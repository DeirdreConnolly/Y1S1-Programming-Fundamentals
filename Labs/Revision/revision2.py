# counting while
print("Demo counting while loop")
n = 1;
while n < 3:
    print("n is" + str(n))
    n = n + 1

#   while with boolean   +  string length +  letters in string

#   get string input where word must start with A

print("While loop and boolean")
valid = False
while not valid:
    name = input("enter a name starting with A")
    name = name.upper()
    if len(name) > 0 and name[0] == 'A':
        valid = True

# while  using try except  +


print("While loop check for int type - using try except \n")
validInteger = False
while validInteger == False:
    try:
        num = int(input("Enter an even number"))
        validInteger = True
    except:
        print("Enter a number")

#
list = ""
list = list + "help"
# counting while to get a list of names
n = 0

print("While loop check for int type - using try except \n")
list = "Names\n-------\n"
while n < 3:
    name = input("enter a name to add to the list")
    list = list + name + "\n"
    n = n+ 1
print(list)
#  runing total
n = 0
total = 0
while n < 3:
    num = int(input("Enter a number to add to total"))
    total += num
    n = n+ 1
print("total is " + str(total))
average = total/3
print("average is " + str(average))

#  find  max -  add if statement in loop
#  find min - add if statement in loop

print("for loop - using range")
# for loop
for i in range(2,5,1):
    print (i)

print("for loop - using list")
for i in [4,8,11]:
    print (i)
# for
print("for loop - for letters in a word")
name = "alex"
for letter in name:
    print (letter)


print("accessing letters in words")
name = "belinda"
print("first letter is " + name[0])
print("second letter is " + name[1])
length = len(name)
last = length - 1
print("last letter is " + name[last])

# Stromng
#  cat
# for string

word = "cat"
length = len(word)

# x = word{0]}