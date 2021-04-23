import random

print("Welcome to GuessingGame by.Ley")
answer = random.randrange(0,100)

quiz = int(input("What's your number? : "))

while answer != quiz:

    if quiz > answer:
        print("Lower")
    elif quiz < answer:
        print("Higher")
    else:
        break
    quiz = int(input("That's not right, AGAIN!!! : "))

print("You win!!!")

