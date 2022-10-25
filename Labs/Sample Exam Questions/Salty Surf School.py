# Filename:      Salty Surf School.py
# Author:        Deirdre Connolly
# Student ID:    R00112962
# Description:   Sample Exam Question - Salty Surf School

# Variables and Constants
BEGINNER = 10.25
ADVANCED = 14.75
cost = 0
DISCOUNT = 2


# Input from Client
print("~~~~~~~~~~ The Salty Sea Surf ~~~~~~~~~~")
firstName = input("Please enter your first name: ")
surname = input("Please enter your surname: ")
level = int(input("Please enter your level:" + "\n" +
          "\t" + "1. Beginner" + "\n" +
          "\t" + "2. Advanced" + "\n" +
          "==> "))


# Cost
    # BEGINNER = 10.25
    # ADVANCED = 14.75
valid = False
while not valid:
    if level == 1:
        cost = BEGINNER
        levelType = "Beginner"
        print("Beginner lesson selected.")
        break
    elif level == 2:
        cost = ADVANCED
        levelType = "Advanced"
        print("Advanced lesson selected.")
        break
    else:
        print("Invalid input. Please try again.")


# Discount
while not valid:
    discountCode = input("Please enter discount code: ").upper()
    if len(discountCode) == 4 and discountCode[0] == 'S':
        valid = True
        finalCost = (cost - DISCOUNT)
        print("€2 discount applied.")
    else:
        print("Invalid code.")

print("Total cost: " + "€" + str(finalCost))


# Write to File
newFile = open(firstName + surname + ".txt", "w")

booking = ("~~~~~~~~~~ The Salty Sea Surf ~~~~~~~~~~" + "\n" +
           "Name" + "\t" + "\t" + "Surname" + "\t" + "\t" + "Level" + "\t" + "\t" + "Cost" + "\n" +
           ("-" * 40) + "\n" +
           firstName + "\t" + "\t" + surname + "\t" + levelType + "\t" + "€" + str(finalCost))

newFile.write(booking)

newFile.close()