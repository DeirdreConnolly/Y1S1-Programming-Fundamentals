# Filename:      DeirdreConnolly_Exam1.py
# Author:        Deirdre Connolly
# Student ID:    R00112962
# Description:   Exam 1: Tour Company Example

try:
    destination = input("Enter name of destination: ").upper()

    if not destination.isalpha():
        print("Invalid input. Please try again.")

    else:
        distance = int(input("Enter distance to destination in km: "))
        returnDistance = distance * 2

        print("-" * 40)

        print("Destination: " + "\t\t" + destination)
        print("Distance Return: " + "\t" + str(returnDistance) + "km")

        priceAdult = 8 + (returnDistance * .1)      # €8 charge for lunch
        priceAdult_formatted = format(priceAdult, ".2f")
        print("Adult Return: " + "\t\t" + "€" + str(priceAdult_formatted))

        priceChild = priceAdult / 2     # child ticket is half of adult
        priceChild_formatted = format(priceChild, ".2f")
        print("Child Return: " + "\t\t" + "€" + str(priceChild_formatted))

        print("Lunch is included in price.")

        if distance >= 100:
            print("**Free snacks provided!**")
        else:
            print("Snacks available for purchase.")

        print("-" * 40)

except:
    print("Invalid input. Please try again.")

