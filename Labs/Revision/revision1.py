#  variables
#  constants
# types
#  if statement

name_of_person = "alice"
age_in_2012 = 5
WEITGHTING_FOR_XXX = 1.567
isGreaterThan10 = False
valid = False
type(name_of_person)
print(format(WEITGHTING_FOR_XXX, "0.1f"))
#   input
#  in t input

# try  except

num = 5 * 4
print(num)

ans = 5/4
print(ans)

ans2 = 5 // 4
print(ans2)

ans3 = 5 % 4
print(ans3)

# check if no is divisible by  2 or 3

num = 7

div = 7/2
if div == 0:
    print("its divisible by 3")
else:
    print("its not divisible by 3")


num = 6

if num < 0 :
    print("its negative")
elif num < 10:
    print("its a sigle digit")
else:
    print("positive double digit")

# getting input for different type + print int or floats
name = input("enter name")
print(name)

age = int("enter integer")
print(str(age))


weight = float("enter weight")
print(str(weight))

print(format(weight, "0.2f"))