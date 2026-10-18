def main():
    cal = input("expression: ").split()
    print(value(cal))


def value(cal):
    if cal[1] == "+":
        return float(cal[0]) + float(cal[2])
    elif cal[1] == "-":
        return float(cal[0]) - float(cal[2])
    elif cal[1] == "*":
        return float(cal[0]) * float(cal[2])
    elif cal[1] == "/":
        return int(cal[0]) / int(cal[2])


main()



