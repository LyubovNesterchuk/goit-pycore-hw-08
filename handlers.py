import pickle
from datetime import timedelta, date, datetime

from color_function import success, error, info
from models import Record, AddressBook
from ui import commands
from utils import input_error
from formatters import format_contact, format_all_contacts, format_birthdays

def get_record_or_fail(book: AddressBook, name: str) -> Record:
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    return record


@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Give me name and phone please.")

    name, phone = args

    temp_record = Record(name)
    temp_record.add_phone(phone)  

    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)

    return success(message)



@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args

    record = get_record_or_fail(book, name)
    record.edit_phone(old_phone, new_phone)

    return success("Contact updated.")



@input_error
def show_phone(args, book: AddressBook):
    name = args[0]

    record = get_record_or_fail(book, name)

    if not record.phones:
        return success(f"Contact '{name}' has no phone numbers.")
    
    return success("; ".join(p.value for p in record.phones))



@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args

    record = get_record_or_fail(book, name)
    record.add_birthday(birthday)

    return success("Birthday added.")



@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]

    record = get_record_or_fail(book, name)

    if not record.birthday:
        return error("Birthday not set.")

    return success(record.birthday.value)



@input_error      
def birthdays(args, book: AddressBook):
    today = date.today()
    upcoming = []

    for record in book.data.values():
        if not record.birthday:
            continue

        birthday_str = record.birthday.value
        bday = datetime.strptime(birthday_str, "%d.%m.%Y").date()
        bday = bday.replace(year=today.year)

        if bday < today:
            bday = bday.replace(year=today.year + 1)

        if 0 <= (bday - today).days <= 7:
            if bday.weekday() == 5:
                bday += timedelta(days=2)
            elif bday.weekday() == 6:
                bday += timedelta(days=1)

            upcoming.append((bday, record.name.value))

    upcoming.sort(key=lambda x: x[0])

    return success(format_birthdays(upcoming))



@input_error
def show_contact(args, book: AddressBook):
    name = args[0]

    record = get_record_or_fail(book, name)
    # return success(str(record))
    return success(format_contact(record))



@input_error
def show_all(book: AddressBook):
#     if not book.data:
#         return error("No contacts saved.")
#     return success("\n".join(str(record) for record in book.data.values()))
    return success(format_all_contacts(book.data.values()))


@input_error
def remove_contact(args, book: AddressBook):
    name = args[0]

    print(error(f"Are you sure you want to delete contact '{name}'? (yes/no): "))
    confirm = input().strip().lower()

    if confirm not in ("y", "yes"):
        return success("Deletion cancelled.")

    book.delete(name)

    return success(f"Contact {name} removed.")



@input_error
def remove_phone(args, book: AddressBook):
    name, phone = args

    record = get_record_or_fail(book, name)

    print(error(f"Delete phone {phone} for {name}? (yes/no): "))
    confirm = input().strip().lower()

    if confirm not in ("y", "yes"):
        return success("Deletion cancelled.")

    record.remove_phone(phone)

    return success(f"Phone {phone} removed for {name}.")



@input_error
def say_hello():
    return info("How can I help you?")



@input_error
def show_help():
    return commands



def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
         pickle.dump(book, f)




def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
    


