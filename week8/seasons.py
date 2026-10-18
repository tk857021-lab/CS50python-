from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    birth = get_birthdate(input("Date of Birth: "))
    print(minutes_in_words(birth))


def get_birthdate(s):
    try:
        return date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")


def minutes_in_words(birth):
    days = (date.today() - birth).days
    minutes = round(days * 24 * 60)
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
