"""Classe_Objects"""

class Student:
    #attributes:
    college_name = "IIT Bombay"

    def __init__(self, name,age,dob):
        print("Constructor has been called")
        self.name = name
        self.age = age
        self.dob = dob

    def print_info(self, name, age, dob):
        print("Student name: "+name)
        print("Student age: "+age)
        print("Student DOB: "+dob)

student_1 = Student("Raj","20","9/05/2000")
student_1.print_info("Raj","20","9/05/2000")

