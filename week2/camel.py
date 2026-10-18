


def main():
    camel = input("camelCase: ")
    print(snake_case(camel))


def snake_case(camel):
    result = ""
    for char in camel:
        if char.isupper():
            result += "_" + char.lower()    # what goes before and after the lowercase letter?
        else:
            result += char
    return result


main()
