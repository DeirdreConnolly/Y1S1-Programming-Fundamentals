#Q1
for i in range (1, 21):
    print(i, end=",")

print(end="\n")

#Q2
for i in range (20, 0, -1):
    print(i, end=",")

print(end="\n")

#Q5
num = int(input("Enter a number: "))
limit = int(input("Enter a second number: "))

for i in range (1, limit):
    print(num, "x", i, "=", num * i)

#Q6
word = input("Enter a word: ")
copy = ""
reverse = ""
for i in word:
    print(i)
    copy = copy + i
    reverse = reverse + i


