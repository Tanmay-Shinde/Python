Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
- Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
- Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("Enter your name: ")
age = input("Enter your age: ")
year = input("What year is it now? ")

age = int(age)
year = int(year)

t = 100 - age
year2 = year + t;

n = input("Enter a number: ")
n = int(n)

i = int('1')
while i <= n:
  print("You will turn 100 in the year ",year2,"\n")
  i+=1
  
