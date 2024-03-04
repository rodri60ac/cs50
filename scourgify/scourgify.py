import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few arguments")
if len(sys.argv) > 3:
    sys.exit("Too many arguments")

students = []

output_file = open(sys.argv[2], "w",newline="")
writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
writer.writeheader()

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last,first = row['name'].split(",")
            students.append({"first": first.lstrip(), "last": last, "house": row["house"]})
            writer.writerow({"first": first.lstrip(), "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit("File Not Found")

