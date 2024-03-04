camel = input("camelCase: ")

snake = ""

for i in range(len(camel)):
    if camel[i].isupper() is True:
        snake = snake + "_" + camel[i].lower()
    else:
        snake = snake + camel[i]

print("snake_name: " + snake)