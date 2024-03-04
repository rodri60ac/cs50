def main():
    tm = input("What time is it? ")
    conv_time = convert(tm)
    
    if 7.0 <= conv_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= conv_time <= 13.0:
        print("lunch time")
    elif 18.0 <= conv_time <= 19.0:
        print("dinner time")
    else:
        print("not time for any meal")


def convert(time):
    h,m = time.split(":")
    conv = int(h) + (int(m)/60)
    return conv

if __name__ == "__main__":
    main()