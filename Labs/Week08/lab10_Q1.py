lumpSum = float(input("Enter the amount of your lump sum: €"))
savingsTarget = float(input("Enter your savings target: €"))
interest = 1.07

print("Lump sum:", "€", format(lumpSum, ".2f"))
print("Savings target:", "€", format(savingsTarget, ".2f"))

year = 0
while lumpSum <= savingsTarget:
    year = year + 1
    lumpSum = lumpSum * interest
    print("Year", year, "€" + format(lumpSum, ".2f"))





