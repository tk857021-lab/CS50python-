
def main():
    time = input("What time is it? ")
    total = convert(time)

    if 7 <= total <= 8:
        print("breakfast time")
    elif 12 <= total <= 13:
        print("lunch time")
    elif 18 <= total <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    total = int(hours) + int(minutes) / 60
    return total


if __name__ == "__main__":
    main()
