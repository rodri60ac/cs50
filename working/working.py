import re
import sys


def main():
    print(convert(input("Hours: ")))

conversion = {
    "12AM" : "00",
    "1AM" : "01",
    "2AM" : "02",
    "3AM" : "03",
    "4AM" : "04",
    "5AM" : "05",
    "6AM" : "06",
    "7AM" : "07",
    "8AM" : "08",
    "9AM" : "09",
    "10AM" : "10",
    "11AM" : "11",
    "12AM" : "12",
    "1PM" : "13",
    "2PM" : "14",
    "3PM" : "15",
    "4PM" : "16",
    "5PM" : "17",
    "6PM" : "18",
    "7PM" : "19",
    "8PM" : "20",
    "9PM" : "21",
    "10PM" : "22",
    "11PM" : "23",
    "12PM" : "24",
}

def convert(s):
    if hours := re.search(r"(([0-9])?[0-9])(:[0-5][0-9])? (AM|PM) to (([0-9])?[0-9])(:[0-5][0-9])? (AM|PM)", s):
        if int(hours.group(1)) > 12 or int(hours.group(5)) > 12:
            raise ValueError
        if hours.group(3) == None and hours.group(7) == None:
            return conversion.get(hours.group(1) + hours.group(4)) + ":00" + " to " + conversion.get(hours.group(5) + hours.group(8)) + ":00"
        if hours.group(3) == None:
            return conversion.get(hours.group(1) + hours.group(4)) + ":00" + " to " + conversion.get(hours.group(5) + hours.group(8)) + hours.group(7)
        if hours.group(7) == None:
            return conversion.get(hours.group(1) + hours.group(4)) + hours.group(3) + " to " + conversion.get(hours.group(5) + hours.group(8)) + ":00"
    else:
        raise ValueError


...


if __name__ == "__main__":
    main()
