#Filename: lab04_user_input
#Author: Deirdre
#Description: Doing calculations with user input

name = input("Enter your name: ")
banner = name + name  + name + name

age = int(input("Enter your age: "))
print(age)

ageDoubled = age  * 2
print(ageDoubled)

gravity = float(input("Gravity on Earth: "))

gravityMoonMul=.166
gravityMoon= gravity * gravityMoonMul
print(gravityMoon)

Sum1 = (4 * 5 * 3) - 1
Sum2 = 4 * 5 * (3 - 1)

print(Sum1)
print(Sum2)


