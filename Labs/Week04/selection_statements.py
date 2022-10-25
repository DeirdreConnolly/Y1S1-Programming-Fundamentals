#Filename: selection_statements.py
#Author: Deirdre
#Description: getting your program to make decisions

import math

x = int(input("Enter a number between 1 and 4: "))

n1 = "Winter"
n2 = "Spring"
n3 = "Summer"
n4 = "Autumn"

if x == 1:
    print(n1)

if x == 2:
    print(n2)

if x == 3:
    print(n3)

if x == 4:
    print(n4)

elif 1 <= x >= 4:
    print("Error. Read the question again.")


n3 = int(input("Enter a number: "))
n4 = int(input("Enter another number: "))

if n3 == n4:
    print(math.sqrt(n3+n4))

if n3 != n4:
    print(math.sqrt(n3), math.sqrt(n4))









n5 = int(input("Enter an integer: "))

if n5 == 10:
    print("Yay! It's equal to 10.")
