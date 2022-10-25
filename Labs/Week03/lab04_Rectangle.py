#Filename: lab04_Rectangle
#Author: Deirdre
#Description: Rectangle

widthRectangle = int(input("Enter width of rectangle: "))
lengthRectangle = int(input("Enter length of rectangle: "))

areaRectangle = widthRectangle * lengthRectangle
perimeterRectangle = widthRectangle + widthRectangle + lengthRectangle + lengthRectangle

print("Width = " + str(widthRectangle))
print("Length = " + str(lengthRectangle))
print("Area = " + str(areaRectangle))
print("Perimeter = " + str(perimeterRectangle))