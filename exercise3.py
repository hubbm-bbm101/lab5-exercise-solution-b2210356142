import random
number = random.randint(1,20)

while True:
    guess = int(input("enter a number"))
    if guess == number:
        print("correct")
        break   
    elif guess > number:
        print ("decrease your number")
    elif guess<number:
        print ("increase your number")


