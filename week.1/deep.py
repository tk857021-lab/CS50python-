deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
if deep == "42".strip():
    print("Yes")
elif deep == "Forty Two":
    print("Yes")
elif deep == "FoRty TwO":
    print("Yes")
elif deep == "forty-two":
    print("Yes")
elif deep == "forty two":
    print("Yes")
else:
    print("No")


