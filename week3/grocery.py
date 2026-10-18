
def main():
    items = {}

    while True:
        try:
            item = input().upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1   # what key, what starting count?
        except EOFError:
            break

    for item in sorted(items):
        print(f"{items[item]} {item}")    # what order — count first or item first?


main()
