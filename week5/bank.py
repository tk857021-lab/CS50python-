def main():
   greet = input("greet: ")
   print(f"${value(greet)}")

def value(greet):
   greet = greet.lower()
   if greet.startswith("hello"):
        return 0
   elif greet.startswith("h"):
        return 20
   else:
       return 100

main()
