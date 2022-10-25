try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    ans1 = (age - 5)
    ans2 = (10 / ans1)
    print(ans2)

    newFile = open("answers.txt", "w")
  #  newFile.write("Name: " + name + "\n" + "Age: " + str(age) + "\n" + str(ans2) + "\n")

    name = name + 5
    #newFile.write(5)

    newFile.close()

except IOError:
    print("IO error")
except PermissionError:
    print("Permission error")
except TypeError as err:
    print("Error - incorrect type", err)
except ValueError:
    print("Error - incorrect value")
except ZeroDivisionError:
    print("Error - cannot divide by zero")
except:
    print("Error")
