#Filename: lab05_shopping
#Author: Deirdre
#Descpription: Calculations with user input

costBread = float(input("Enter cost of bread: "))
costMilk = float(input("Enter cost of milk: "))
discount10 = .1
numBread = int(input("Enter amount of bread bought: "))
numMilk = int(input("Enter amount of milk bought: "))

totalCost = (costBread * numBread) + (costMilk * numMilk) * (1 - discount10)
totalCost_formatted = format(totalCost, ".2f")

bill = "Your total bill is: €" + totalCost_formatted
print(bill)
