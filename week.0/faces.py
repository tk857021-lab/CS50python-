from cs50 import get_string


def main():
    text = get_string("Before: ")
    print("After: " + convert(text))


def convert(s):
    s = s.replace(":)", "🙂")   # replace :) with 🙂
    s = s.replace(":(", "🙁")   # replace :( with 🙁
    return s


main()
