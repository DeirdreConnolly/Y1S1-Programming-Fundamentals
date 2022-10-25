#Filename: menu.py
#Author: Deirdre
#Description: using selection statements with a menu

cheeseBurger = 2.45
hamBurger = 2.35
chickenBurger = 3.65
chargeBurger = 0.0

burgerOrder = int(input("What burger do you want, 1 2 3? "))
print(burgerOrder)

if burgerOrder == 1:
    chargeBurger = cheeseBurger
    print("Cheeseburger is " + str(cheeseBurger))

elif burgerOrder == 2:
    chargeBurger = hamBurger
    print("Hamburger is " + str(hamBurger))

elif burgerOrder == 3:
    chargeBurger = chickenBurger
    print("ChickenBurger is " + str(chickenBurger))

print("Thank you for your order. Your total is ", float(chargeBurger))


smallChips = 2.90
largeChips = 3.50
curryChips = 3.85
chargeChips = 0.0

chipsOrder = int(input("What chips do you want, 1 2 3? "))
print(chipsOrder)

if chipsOrder == 1:
    chargeChips = smallChips
    print("Small chips are " + str(smallChips))

elif chipsOrder == 2:
    chargeChips = largeChips
    print("Large chips are " + str(largeChips))

elif chipsOrder == 3:
    chargeChips = curryChips
    print("Curry chips are " + str(curryChips))

print("Thank you for your order. Your total is ", float(chargeChips))



