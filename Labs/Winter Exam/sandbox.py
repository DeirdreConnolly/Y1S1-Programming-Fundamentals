# Filename:      DeirdreConnolly.py
# Author:        Deirdre Connolly
# Student ID:    R00112962
# Description:   Winter Exam (50%) - Library App


# Constants and Variables
BOOK_LIMIT = 6
membershipID = ""
booksBorrowed = 0
valid = False


# User Input
print("~~~~~~~~~~~~~~ Library App ~~~~~~~~~~~~~")
for member in range(1,5):
    while True:
        membershipID = input("Membership ID: ").upper()
        if len(membershipID) == 4 and membershipID[0].isalpha():
            valid = True
            break
        else:
            print("Invalid format. Please try again.")

    while True:
        booksBorrowed = int(input("Books borrowed: "))
        if booksBorrowed <= BOOK_LIMIT:
            valid = True
            break
        else:
            print("You have reached the limit of books.")

    while True:
        outstandingFine = input("Outstanding fine: €")
        if not outstandingFine.isalpha():
            valid = True
            break
        else:
            print("Invalid format. Please try again.")


# Borrowed Books Information
    i = 0
    while booksBorrowed <= BOOK_LIMIT:
        i = i + 1
        if booksBorrowed == 0:
            print(membershipID + " has borrowed no books.")
            break
        elif booksBorrowed == BOOK_LIMIT:
            print(membershipID + " has reached the limit of books.")
            break
        elif booksBorrowed < BOOK_LIMIT:
            print(membershipID + " can still borrow " + str(BOOK_LIMIT - booksBorrowed) + " book(s).")
            break
        else:
            print("Invalid input. Try again.")
    print("~" * 40)


# Average Number of Books on Loan
    i = 0
    members = i + 1
    average = (booksBorrowed / members)
    average_formatted = format(average, ".0f")
    totalFines = outstandingFine          # how to get each outstandingFine and add together?
    print("Average number of books borrowed: " + str(average_formatted))
    if booksBorrowed == BOOK_LIMIT:
        print(str(members) + " members have borrowed all " + str(BOOK_LIMIT) + " books.")
    else:
        print("No members have borrowed all " + str(BOOK_LIMIT) + " books.")
    print("Total fines amount to: " + "€" + str(totalFines))
    print("~" * 40)


# Write to File
    newFile = open("stats_sandbox.txt", "w")

    largestFines = ("Largest fine is €" + str(outstandingFine) + " owed by: " + "\n" +
                    "\t" + str(membershipID))

    newFile.write(largestFines)

    newFile.close()