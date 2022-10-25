#Filename: lab05_sandwiches
#Author: Deirdre
#Descpription: Calculations with user input

costSandwich = float(input("Enter cost of sandwich: €"))
reduction = .2
newCost = costSandwich * (1 - reduction)
sign = "Sandwiches reduced today by 20%"

costSandwich_formatted = format(costSandwich, ".2f")
newCost_formatted = format(newCost, ".2f")

msg = sign + " " + "from" +  " " + "€" + costSandwich_formatted +  " " + "to" +  " " + "€" + str(newCost) + "."
print(msg)
