"""File handling"""

#Reading a file

file = open("myFile.txt","r")
print(file.read())

file = open("myFile.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())

file = open("myFile.txt","r")
for x in file:
    print(x)

#Creating a file

file = open("newFile.txt","w")
file.write("content")
file.write("More content")

file = open("newFile.txt","a")
file.write("Appended Content")
file = open("newFile.txt","a")
