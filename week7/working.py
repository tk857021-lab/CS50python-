import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = r"(\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.fullmatch(f"{time} to {time}", s)
    if not match:
        raise ValueError
    start = to_24(*match.group(1, 2, 3))
    end = to_24(*match.group(4, 5, 6))
    return f"{start} to {end}"


def to_24(hour, minute, meridian):
    hour = int(hour)
    minute = int(minute) if minute else 0
    if not (1 <= hour <= 12) or minute > 59:
        raise ValueError
    if meridian == "PM" and hour != 12:
        hour += 12
    elif meridian == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()