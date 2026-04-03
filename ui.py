from color_function import  info, greet


welcome_banner = '''
  ___          _     _              _     _           _   
 / _ \        (_)   | |            | |   | |         | |  
/ /_\ \___ ___ _ ___| |_ __ _ _ __ | |_  | |__   ___ | |_ 
|  _  / __/ __| / __| __/ _` | '_ \| __| | '_ \ / _ \| __|
| | | \__ \__ \ \__ \ || (_| | | | | |_  | |_) | (_) | |_ 
\_| |_/___/___/_|___/\__\__,_|_| |_|\__| |_.__/ \___/ \__|
'''

commands = '''
1) hello - greet the assistant bot
2) add username phone - add a new contact with name and phone number
3) change username old_phone new_phone- change the phone number for an existing contact
4) phone username - show the phone number of the contact
5) add-birthday username DD.MM.YYYY - add a birthday for the specified contact
6) show-birthday username - show the birthday of the specified contact
7) birthdays - show birthdays for the next 7 days with the dates they should be congratulated
8) remove-phone username phone - remove a phone number
9) remove-contact username - remove entire contact
10) show username - display full contact details (name, phones, birthday)
11) all - show all saved contacts
12) help - show this help menu
13) exit or close - exit the application
''' 

def init():
    print(greet(welcome_banner))
    print(info(commands))
    print()