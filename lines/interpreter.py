expression = input("Expression: ")
x,y,z = expression.split()

if y == "+":
    print("{:.1f}".format((int(x) + int(z))))
elif y == "-":
    print("{:.1f}".format((int(x) - int(z))))
elif y == "*":
    print("{:.1f}".format((int(x) * int(z))))
elif y == "/":
    print("{:.1f}".format((int(x) / int(z))))