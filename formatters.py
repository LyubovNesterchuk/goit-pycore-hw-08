def format_contact(record):
    phones = ";".join(p.value for p in record.phones) if record.phones else "-"
    birthday = record.birthday.value if record.birthday else "-"

    return (
        f"\n{'='*30}\n"
        f"👤 {record.name.value}\n"
        f"📞 {phones}\n"
        f"🎂 {birthday}\n"
        f"{'='*30}\n"
    )


def format_all_contacts(records):
    if not records:
        return "No contacts saved."

    rows = []

    for record in records:
        phones = ";".join(p.value for p in record.phones) if record.phones else "-"
        birthday = record.birthday.value if record.birthday else "-"

        rows.append((record.name.value, phones, birthday))

    name_w = max(len("NAME"), max(len(r[0]) for r in rows))
    phone_w = max(len("PHONES"), max(len(r[1]) for r in rows))
    bday_w = max(len("BIRTHDAY"), max(len(r[2]) for r in rows))

    header = f"{'NAME':<{name_w}} | {'PHONES':<{phone_w}} | {'BIRTHDAY':<{bday_w}}"
    separator = "-" * len(header)

    lines = [header, separator]

    for name, phones, birthday in rows:
        lines.append(f"{name:<{name_w}} | {phones:<{phone_w}} | {birthday:<{bday_w}}")

    return "\n".join(lines)


def format_birthdays(upcoming):
    if not upcoming:
        return "No upcoming birthdays."

    return "\n".join(
        f"🎉 Don't forget to congratulate {name} {bday.strftime('%d.%m.%Y')} !"
        for bday, name in upcoming
    )