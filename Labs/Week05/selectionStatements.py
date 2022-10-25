#Filename: selectionStatements.py
#Author: Deirdre
#Description: using AND, OR, NOT

n1 = "John"
n2 = "George"
n3 = "Ringo"
n4 = "Paul"

name = input("Enter a name: ")

if name == n1 or name == n2 or name == n3 or name == n4:
    print("Hey, that's the name of a Beatle!")

else:
    print("That's a nice name.")


temp = int(input("Enter a temperature in Celsius: "))
print(temp)

if temp <8:
    print("Brrr, it's cold.")

elif temp >= 8 and temp <= 14:
    print("It's a mild day.")

elif temp >= 15 and temp <= 20:
    print("It's a warm day.")

elif temp >= 21:
    print("It's a hot day, be careful of the sun!")


goals = int(input("How many goals were scored? "))
print(goals)

if goals == 0:
    print("This game was a bore draw!")

elif 1 <= goals <= 2:
    print("Not the most interesting game.")

elif 3 <= goals <= 5:
    print("It was a very interesting game.")

elif goals >=6:
    print("What an unmissable game!")


s1 = int(input("Enter length of side 1: "))
s2 = int(input("Enter length of side 2: "))
s3 = int(input("Enter length of side 3: "))
print(s1, s2, s3)

if s1 == s2 and s2 == s3 and s1 == s3:
    print("Equilateral triangle")

elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles triangle")

elif s1 != s2 or s2 != s3 or s1 != s3:
    print("Scalene triangle")


a1 = input("Enter a letter: ")
print(a1)

if a1 == "a" or  a1 == "e" or  a1 == "i" or  a1 == "o" or  a1 == "u":
    print("That letter is a vowel.")

elif a1 == "y":
    print("Sometimes Y is a vowel, such as in rhythm. Sometimes Y is a consonant, such as in \'yellow\'.")

elif a1 != "a" or  a1 == "e" or  a1 == "i" or  a1 == "o" or  a1 == "u":
    print("That letter is a consonant.")




