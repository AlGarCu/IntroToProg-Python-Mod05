# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Change Log: (Who, When, What)
#   Alejandro Garcia, 5/18/2024, Created Script for A05
# ------------------------------------------------------------------------------------------ #

# Importing json package

import json

# Defining the Data Constants and including Type hints

MENU: str = '''\
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Defining the Data Variables and including Type hints
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
json_data: str = ''
file = None # Type hint omitted here as potential bug pointed in Module 04 Notes
menu_choice: str = ''
student_data: dict = [] # This table will hold the student data dictionary rows for each individual
students: list = [] #  One row per Student
# Reading the existing contents from the .csv file into a two-dimensional list of lists (i.e. a table)
try:
    file = open("Enrollments.json", 'r')
    students = json.load(file)
    file.close()
    print(students)
except FileNotFoundError:
    print("File Not Found")
# Present the menu of choices and Process the data
while True: # Initializing the while loop
    print(MENU)
    menu_choice = input("What would you like to do? ")
    if menu_choice == '1': #Initializing the if/elif conditional statements
    # Menu 1 -- Input user data
        try:
            student_first_name = input ("Enter student's first name ")
        except ValueError:
            print("Invalid input")
        try:
            student_last_name = input ("Enter student's last name ")
        except ValueError:
            print("Invalid input")
        course_name = input ("Enter course name ")
        json_data = f"Name: {student_first_name} Last Name: {student_last_name} Course: {course_name}" #json_data built from option 1
        student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name.strip() }
        students.append(student_data) #adding collected data into the list of lists (as a dictionary row)
    elif menu_choice == '2':
    # Menu 2 -- Present the current data
        print("The last student's data collected is:")
        print(json_data)
        print("The full list of student data collected follows:")
        for entries in students:
            print(f"Name: {entries['FirstName']}, Last Name: {entries['LastName']}, Course: {entries['CourseName']}")
    elif menu_choice == '3':
    # Menu 3 -- Save the data to a file and display it
        try:
            file = open(FILE_NAME,"w")
            json.dump(students, file)
            file.close()
            print("The following data was added to the file:")
            print(json_data)
            print("The full list of data stored in the file follows:")
        except FileNotFoundError:
            print("File Not Found")

# Menu 4 -- Stop the loop
    elif menu_choice == '4': #Granting the option to exit the while loop via choice 4
        break
    else:
        print("Please select a valid option")
        continue #Reverting back to the start of the while loop for any invalid choice and giving error message






