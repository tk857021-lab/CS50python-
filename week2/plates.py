def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: length check
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: must be alphanumeric only (no spaces, no punctuation)
    if not s.isalnum():
        return False

    # Rule 3 & 4 & 5: walk through characters, track letters vs digits
    digit_started = False
    digit_count = 0

    for i, char in enumerate(s):
        if char.isalpha():
            if digit_started:
                return False   # letters can't come after digits have started
        elif char.isdigit():
            if not digit_started:
                digit_started = True
                if char == "0":   # first digit can't be this
                    return False
            digit_count += 1
            if digit_count > 4:    # max digits allowed
                return False

    return True


main()
