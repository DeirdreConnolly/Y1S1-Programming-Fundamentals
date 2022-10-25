n1 = "JOHN"
n2 = "GEORGE"
n3 = "RINGO"
n4 = "PAUL"

name = str(input("Enter a name: ")).upper()

if name == n1 or name == n2 or name == n3 or name == n4:
    print("Hey, that's the name of a Beatle!")
elif name.isalnum():
    print("Invalid input.")
else:
    print("That's a nice name.")

try:
    number = int(input("Enter a number: "))
except:
    print("This is not a number.")