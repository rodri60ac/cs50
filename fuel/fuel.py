while True:
    try:
        fract = input("Fraction: ")
        x,y = fract.split("/")
        x = int(x)
        y = int(y)

        if x > y:
            pass
        elif y == 0:
            pass
        else:
            out = round((round(x / y,2))*100)
            if out >= 99:
                print("F")
                break
            elif out <= 1:
                print("E")
                break
            else:
                print(f"{out}%")
                break

    except ValueError or ZeroDivisionError:
        pass