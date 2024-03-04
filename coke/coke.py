amountdue = 50

while amountdue > 0:
    print("Amount Due:", amountdue)
    insert = int(input("Insert Coin: "))
    if insert in [25,10,5]:
        amountdue = amountdue - insert


print("Changed Owned:", abs(amountdue))