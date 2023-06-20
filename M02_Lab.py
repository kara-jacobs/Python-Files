"""
Program: M02_Lab.py
Title: Student GPA Evaluator
Author: Kara Jacobs
Date last modified: 06/19/2023

Description: This program will prompt the user for a student's last name, 
with the option to quit if they enter ZZZ. If a last name is entered, the 
program then prompts the user to enter a first name and a GPA. If the GPA 
is 3.5 or higher, a message appears saying that the student has made the 
Dean's List. If the GPA is 3.25 or higher, a message appears saying that 
the student has made the Honor Roll.

Variables:
    last_name (a student's last name)
    first_name (a student's first name)
    GPA (a student's GPA)
"""

# The user is prompted to enter a last name or ZZZ to quit.
last_name = input("Please enter a student's last name or enter ZZZ to quit: ")

# As long as ZZZ is not entered, the program loops.
while last_name != "ZZZ":
    
    # The user is prompted to enter a first name and a GPA.
    first_name = input("Please enter student's name: ")
    GPA = float(input("Please enter your GPA: "))

    # The GPA is evaluated to see if the student has made the Dean's List or Honor Roll.
    if GPA >= 3.5:
        print(first_name + " " + last_name + " has a GPA of " + str(GPA) + " and has made the Dean's list!")
    elif GPA >= 3.25:
        print(first_name + " " + last_name + " has a GPA of " + str(GPA) + " and has made the Honor Roll!")
    
    # The user is prompted to enter another last name.
    last_name = input("Please enter another student's last name or enter ZZZ to quit: ")
    
print("End of program.")