#Project 1: School Admin Tool

import csv

def write_in_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","Email ID"])
            
        writer.writerow(info_list)

condition = True
student_num = 1

if __name__ == '__main__':
    while(condition):
        Student_info = input("Enter the student information for student #{} in the following format(Name Age Contact Email: ".format(student_num))
        student_info_list = Student_info.split(' ')

        print("\n The entered information is - \nName: {}\nAge: {}\nContact Number: {}\nEmail ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_check = input("Is the entered information correct? (yes/no): ")
        if choice_check == "yes":
            write_in_csv(student_info_list)
            
            condition_check = input("Do you want to enter the information of other students? (yes/no): ")
            if condition_check == "yes":
                condition = True
                student_num+=1
            else:
                condition = False

        else:
            print("\nPlease enter the correct values again")
