groceries = {}

while True:
    try:
        item = input("Item: ").upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        break

for item in groceries:
    print(groceries[item], item)
