#Filename: lab05_average
#Author: Deirdre
#Descpription: Calculations with user input

resultsEngligh = int(input("Enter English results: "))
resultsMaths = int(input("Enter Maths results: "))
resultsScience = int(input("Enter Science results: "))

total = (resultsEngligh + resultsMaths + resultsScience)
average = int(total) / 3

average_formatted = format(average, "2.0f")

print(average_formatted)




