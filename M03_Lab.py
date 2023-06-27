"""
Program: M03_Lab.py
Title: Vehicle App
Author: Kara Jacobs
Date last modified: 06/26/2023

Description: This app will prompt a user to enter a vehicle type (the only available option is 'car'). 
Once the user enters 'car', they will then be prompted to enter the car's year of manufacture, make, 
model, number of doors, and roof type. After the data is entered, all of the entered information is 
displayed in an easy-to-read format.

Variables:
    vehicle_type (input for the type of vehicle)
    year (the car's year of manufacture - integer)
    make (the car's make)
    model (the car's model)
    doors (number of doors the car has (2 or 4))
    roof (type of car roof (solid or sun roof))
"""

# Defines a class called Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    # Defines Accessor method for the vehicle type
    def get_vehicle_type(self):
        return self.vehicle_type


# Defines a subclass of Vehicle called Automobile
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
    # Defines Accessor method for the car year of manufacture
    def get_year(self):
        return self.year

    # Defines Accessor method for the car make
    def get_make(self):
        return self.make
    
    # Defines Accessor method for the car model
    def get_model(self):
        return self.model
    
    
# This function collects user inputs for the vehicle, and then prints them
def main_program():
    
    # Prompts user to enter the vehicle type, and converts the user input to lower-case. 
    vehicle_type = input("Enter vehicle type, such as car, truck, plane, boat, or broomstick (note: 'car' is currently the only available type): ").casefold()
    # 'Car' is the only available valid vehicle option.
     # The other valid vehicle types (truck, plane, boat, & broomstick) are not available, and raise an error
    while vehicle_type != "car":
        if vehicle_type == "truck":
            print("Truck data entry is not available yet.")
        elif vehicle_type == "plane":
            print("Plane data entry is not available yet.")
        elif vehicle_type == "boat":
            print("Boat data entry is not available yet.")
        elif vehicle_type == "broomstick":
            print("Broomstick data entry is not available yet.")
        vehicle_type = input("Please enter a valid vehicle type (note: 'car' is currently the only available type): ").casefold()
    
    # Prompts user to enter the car's year, and raises an error if the answer is not an integer
    while True:
        try:
            year = int(input("Enter car year of manufacture: "))
            break
        except ValueError:
            print("Please input an integer for the year of manufacture:")  
            continue
    
    # Prompts user to enter the car's make
    make = input("Enter car make: ")
    
    # Prompts user to enter the car's model
    model = input("Enter car model: ")
    
    # Prompts user to enter 2 or 4 for car door number, and loops until a 2 or 4 is entered
    while True:
        try: 
            doors = int(input("Does your car have 2 or 4 doors?: "))
        except ValueError:
            continue
        if doors in (2, 4):
            break

    # Assigns car door number to either "2" or "4"
    if doors == 2:
        doors_num = "2"
    else:
        doors_num = "4"
    
    # Prompts user to enter 1 or 2 for roof type, and loops until a 1 or 2 is entered
    while True:
        try: 
            roof = int(input("Enter 1 if your car roof is solid, or 2 if your car has a sun roof: "))
        except ValueError:
            continue
        if roof in (1, 2):
            break

    # Assigns the roof type to either "solid" or "sun roof"
    if roof == 1:
        roof_type = "solid"
    else:
        roof_type = "sun roof"
        
    #A vehicle object is created
    vehicle1 = Automobile(vehicle_type, year, make, model, doors, roof)

    # Print statements using Accessor methods
    print(" ")
    print(" ")
    print("VEHICLE INFORMATION")
    print("\nVehicle type: ", vehicle1.get_vehicle_type())
    print("\nYear: ", vehicle1.get_year())
    print("\nMake: ", vehicle1.get_make())
    print("\nModel: ", vehicle1.get_model())
    print("\nNumber of doors: ", doors_num)
    print("\nType of roof: ", roof_type) 
    print(" ")
    print(" ")

    # Prompt's user to enter another vehicle's data or to press 'x' to quit app
    exit = input("Press any key to enter another vehicle's data, or press x to exit: ").casefold()
    if exit != "x":
        print(" ")
        print(" ")
        main_program()
    else:
        print(" ")
        print("End of program.")

# The main_program() function is called
main_program()
