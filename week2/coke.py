


def main():
    due = 50
    print(f"Change Owed: {insert_coin(due)}")


def insert_coin(due):
    while due > 0:
        coins = int(input("coin: "))
        if coins == 25:
            due = due - 25
        elif coins == 10:
            due = due - 10
        elif coins == 5:
            due = due - 5

        print(f"Amount Due: {due}")

    return abs(due)


main()
