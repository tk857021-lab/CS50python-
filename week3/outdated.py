import re


def main():
    while True:
        date = input("Date: ").strip()
        try:
            print(convert(date))
            break
        except ValueError:
            continue


def convert(date):
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    match = re.match(r"^([A-Za-z]+) (\d{1,2}), (\d{4})$", date)
    if match:
        month_name, day, year = match.groups()
        if month_name not in months:
            raise ValueError
        month = months[month_name]
        day = int(day)
        if not (1 <= day <= 31):
            raise ValueError
        return f"{year}-{month:02}-{day:02}"

    match = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", date)
    if match:
        month, day, year = match.groups()
        month, day = int(month), int(day)
        if not (1 <= month <= 12):
            raise ValueError
        if not (1 <= day <= 31):
            raise ValueError
        return f"{year}-{month:02}-{day:02}"

    raise ValueError("Invalid date")


main()
