myFile = open("rainfall.txt", "r")
info = myFile.readline(0)
print(info.upper)
total = 0

for line in myFile:
    line = line.rstrip()
    print(line)
    infoList = line.split(",")
    #print(infoList[0])
    #print(infoList[1])

print("-" * 10)

total = (total + float(infoList[1]))
average = total / 3
print("Total rainfall is: " + str(total))
print("Average rainfall is: " + str(average))

print("End")

myFile.close
