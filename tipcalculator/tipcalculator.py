def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    flo = float(d.replace("$",""))
    return flo


def percent_to_float(p):
    perc = float(p.replace("%",""))/100
    return perc


main()
