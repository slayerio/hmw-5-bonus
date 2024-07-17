import random


attempts = 0
while True:
    num1 = random.randint(1,100)
    while True:
        x = int(input("pick a random number between 1-100?"))
        if x > num1:
            print("number too big")
            attempts += 1
        elif x < num1:
            print("number too small")
            attempts += 1
        else:
            print("BINGO")
            break
    print(f"you had {attempts} attempts")
    x = int(input("if you wanna play again, press 1. else put any number"))
    if x == 1:
        continue
    else:
        break

print("thanks for playing!")
