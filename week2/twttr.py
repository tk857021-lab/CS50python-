def main():
    n = input("input: ")
    print(output(n))


def output(n):
    n = n.replace("a", "")
    n = n.replace("e", "")
    n = n.replace("i", "")
    n = n.replace("o", "")
    n = n.replace("u", "")
    n = n.replace("A", "")
    n = n.replace("E", "")
    n = n.replace("I", "")
    n = n.replace("O", "")
    n = n.replace("U", "")
    return n


main()
