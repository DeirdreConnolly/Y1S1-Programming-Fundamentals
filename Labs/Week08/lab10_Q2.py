import random

number = random.randint(1,100)
guess = number - 1

i = 0
while guess != number:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess > number:
        print("Guess lower.")
        i = i + 1
    elif guess < number:
        print("Guess higher.")
        i = i + 1
    elif guess == number:
        print("Yay, you got it!")
