import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
if len(sys.argv) > 2:
    sys.exit("Too many arguments")
if sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

menu = []

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    sys.exit("File Not Found")

print(tabulate(menu,headers="keys",tablefmt="grid"))