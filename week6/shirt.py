import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

ext1 = os.path.splitext(sys.argv[1])[1].lower()
ext2 = os.path.splitext(sys.argv[2])[1].lower()

if ext1 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
elif ext2 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
elif ext1 != ext2:
    sys.exit("Input and output have different extensions")

try:
    photo = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, (0, 0), shirt)
    photo.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
