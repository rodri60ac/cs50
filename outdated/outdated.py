months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        #See if its mm/dd/yyyy
        date = input("Date: ")
        m,d,y = date.split("/")

        m = int(m)
        d = int(d)
        y = int(y)

        if (1 <= m <= 12) and (0 < d <= 31):
            print(f"{y}-{m:02}-{d:02}")
            break
    except:
        try:
            #See if it Month day, year
            date = date.replace(",","")
            m,d,y = date.split()
            day = int(d)
            if m in months and day <= 31:
                month = int(months.index(m))+1
                print(f"{y}-{month:02}-{day:02}")
                break
        except:
            pass