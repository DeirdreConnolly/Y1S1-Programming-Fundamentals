# Filename:     DeirdreConnolly_Project.py
# Author:       Deirdre Connolly
# Student ID:   R00112962
# Description:  Project (25%): Studio Application
# Note:         I had trouble with the validation, I couldn't figure out a way to do it properly.

# Variables and Constants
MAX_PERSONS = 8
SESSION_MUSICIANS_PER_DAY = 100
LEVY = (1 + 0.05)
REDUCTION = (1 - 0.05)
bandMember = ""
instrument = ""
CREDIT_CARD = 1
CASH = 2
CHEQUE = 3
cost = 0
ONE_DAY = 260
TWO_TO_FOUR_DAYS = 240
FIVE_TO_EIGHT_DAYS = 210
NINE_PLUS_DAYS = 200


# Information Gathered From Client
managerName = input("Name: ")
managerEmail = input("Email address: ")
managerPhone = int(input("Phone number: "))
dateStart = input("Start date (dd/mm/yyyy): ")
bandName = input("Band name: ")
bandMembersTotal = int(input("Number of band members: "))
days = int(input("How many days do you need the studio? "))
paymentType = int(input("Will you pay by:" + "\n" +
                        "1. Credit card (5% levy)" + "\n" +
                        "2. Cash (5% discount)" + "\n" +
                        "3. Cheque" + "\n" +
                        "Payment type: "))


# Band Members and Instruments
for i in range(int(bandMembersTotal)):
    i = i + 1
    bandMember = input("Band member "+ str(i) + ": ")
    instrument = input("Instrument " + str(i) + ": ")
    bandMembers = (bandMember + " - " + instrument)
    print(str(i) + ": " + bandMembers)


# Session Musicians
i = 0
sessionMusicians = 0
while int(bandMembersTotal) < int(MAX_PERSONS):
    i = i + 1
    print("You can have a total of 8 people in the room.")
    addSessionMusicians = int(input("How many session musicians (€100 per day) do you want? "))
    if addSessionMusicians <= int(MAX_PERSONS - bandMembersTotal):
        print(str(addSessionMusicians) + " session musicians added.")
        break
    elif addSessionMusicians > int(MAX_PERSONS - bandMembersTotal):
        print("Sorry, you have reached maximum capacity.")
print("-" * 30)


# Calculate Costs - Days
    # ONE_DAY = 260
    # TWO_TO_FOUR_DAYS = 240
    # FIVE_TO_EIGHT_DAYS = 210
    # NINE_PLUS_DAYS = 200
if days == 1:
    costDays = (days * ONE_DAY)
elif 2 >= days <= 4:
    costDays = (days * TWO_TO_FOUR_DAYS)
elif 5 >= days >= 8:
    costDays = (days * FIVE_TO_EIGHT_DAYS)
elif days > 9:
    costDays = (days * NINE_PLUS_DAYS)


# Calculate Costs - Session Musicians
    # SESSION_MUSICIANS_PER_DAY = 100
sessionMusicians = addSessionMusicians
costSessionMusicians = (addSessionMusicians * 100 * days)


# Calculate Costs - Subtotal
costDays = 0
subtotalCost = (costDays + costSessionMusicians)


# Calculate Costs - Payment Type
    # LEVY = (1 + 0.05)
    # REDUCTION = (1 - 0.05)
    # CREDIT_CARD = 1 = LEVY
    # CASH = 2 = REDUCTION
    # CHEQUE = 3
if paymentType == 1:
    print("Payment Type: Credit card")
    totalCost = (subtotalCost * LEVY)
    formattedCost = format(totalCost, ".2f")
elif paymentType == 2:
    print("Payment Type: Cash")
    totalCost = (subtotalCost * REDUCTION)
    formattedCost = format(totalCost, ".2f")
elif paymentType == 3:
    print("Payment Type: Cheque")
    totalCost = (subtotalCost)
    formattedCost = format(totalCost, ".2f")


# Receipt
print("Payment: €" + str(formattedCost))
print("Name: " + managerName)
print("Email: " + managerEmail)
print("Phone: " + str(managerPhone))
print("Start Date: " + dateStart)
print("Days: " + str(days))
print("Band Name: " + bandName)
print("Number of Band Members: " + str(bandMembersTotal))
print("Session Musicians: " + str(sessionMusicians))
print("-" * 30)


# Write to File
receiptPayment = ("Payment: €" + str(formattedCost))
receiptName = ("Name: " + managerName)
receiptEmail = ("Email: " + managerEmail)
receiptPhone = ("Phone: " + str(managerPhone))
receiptStartDate = ("Start Date: " + dateStart)
receiptDays = ("Days: " + str(days))
receiptBandName = ("Band Name: " + bandName)
receiptBandMembersTotal = ("Number of Band Members: " + str(bandMembersTotal))
receiptSessionMusicians = ("Session Musicians: " + str(sessionMusicians))

receipt = (receiptBandName + "\n" +
           receiptPayment + "\n" +
           receiptName + "\n" +
           receiptEmail + "\n" +
           receiptPhone + "\n" +
           receiptStartDate + "\n" +
           receiptDays + "\n" +
           receiptBandMembersTotal + "\n" +
           receiptSessionMusicians)

newFile = open(bandName + ".txt", "w")
newFile.write(receipt)
newFile.close()