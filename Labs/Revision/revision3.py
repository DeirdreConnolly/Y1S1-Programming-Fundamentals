file = open("ex1.txt")
for line in file:
    line = line.rstrip()
    print(line)
    words = line.split()
    print(words[0])
file.close()


newfile = open("data.txt",'w')
newfile.write("Anna\n")
newfile.write(str(20))
newfile.close()