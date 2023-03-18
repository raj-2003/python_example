import random

num=random.randint(1,20)

while True:

    guess=int(input("Enter a number between 1 to 20 : "))

    if guess==num:
        print("You choose correct number")
        break

    elif guess>num:
        print("You choose greater number")

    elif guess<num:
        print("You choose smaller number")
