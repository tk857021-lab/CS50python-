import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

try:
    with open(sys.argv[1]) as infile, open(sys.argv[2], "w") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(",")
            writer.writerow({
                "first": first.strip(),
                "last": last.strip(),
                "house": row["house"],
            })
except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])
