import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break

    except:
        pass

answ = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < answ:
                print("Too small!")
            elif guess > answ:
                print("Too big!")
            else:
                print("Just right!")
                break
    except:
        pass