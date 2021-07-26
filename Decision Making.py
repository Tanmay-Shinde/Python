"""Decision Making"""

#if-else constructs

age = int(input("Enter your age: "))

if age>18:
    print("You can vote")
else:
    print("You cannot vote")

#if-else if constructs

marks = int(input("Enter your marks: "))

if marks > 90:
    print("Distinction")
elif marks > 80:
    print("First Class")
elif marks > 70:
    print("Second Class")
elif marks > 60:
    print("Third Class")
elif marks > 40:
    print("Pass")
else:
    print("Fail")
