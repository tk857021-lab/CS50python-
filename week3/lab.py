def main():
    n = get_int()
    print(f"n is {n}")


def get_int():
 while True:
    try:
       n = int(input(""))
    except ValueError:
         print("bitch put number not a word ")
    else:
          break
 return n


main()
