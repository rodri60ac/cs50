from datetime import date
from datetime import timedelta
import sys
import inflect

p = inflect.engine()

def main():

    print(lived(input("Date of Birth: ")))


def lived(s):
    try:
        born = date.fromisoformat(s)
        today = date.today()
        dif = today - born
        dif_min = p.number_to_words(round(dif.total_seconds() / 60)).capitalize()
        return dif_min + " minutes"
    except:
        sys.exit("Invalid date")

...

if __name__ == "__main__":
    main()
