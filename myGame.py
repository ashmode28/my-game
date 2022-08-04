import random

def guess():
    n = 0
    live = 10
    opinion = False
    answer = random.randint(1,50)
    print("welcome to my third python class project.")
    while n != answer:
        print(f"\n you have {live} more chance to guess it correctly.")
        n = int(input("guess a number from 1 to 50:"))
        if n > answer:
            print("you guessed too high.")
        elif n < answer:
            print("you guessed to low.")
        else:
            opinion = True
        live -= 1
        if live == 0:
            break
    if live == 0 and opinion == False:
        print("timeout.")
    else:
        print("congratula you guessed correctly.")

guess()