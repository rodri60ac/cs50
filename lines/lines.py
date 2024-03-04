import sys

line_count = 0

try:
    if len(sys.argv) != 2 or sys.argv[1][-3:] != ".py":
        sys.exit("Wrong Input")
    else:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.strip() == "" or line[0] == "#":
                    line_count = line_count
                else:
                    line_count += 1
except:
    sys.exit("Error")

print(f"Number of lines: {line_count}")