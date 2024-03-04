import random


def main():
    level = get_level()
    i = 0

    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        trycount = 0
        while trycount < 3:
            guess = int(input(f"{x} + {y} ="))
            if guess == result:
                break
            else:
                if trycount == 2:
                    print(f"{x} + {y} = {result}")
                    break
                else:
                    print("EEE")
                    trycount += 1
        
        i += 1


def get_level():
    #get difficulty leveç from user
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except:
            pass


def generate_integer(level):
    if not level in [1,2,3]:
        raise ValueError('Level needs to be 1,2 or 3')
    elif level == 1:
        return random.randint(1,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
