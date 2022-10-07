import random

""" Defining main functions """

## Defining a function to create a new knight
def create_knight(knights):
    # Determines the size of knights which is changing dynamically
    knights_number = len(knights)

    # Create an object
    knights_data = {}
    print("Lets create a knight!")

    # Set the information up for the knight
    knights_name = str(input("What is the knights name: "))
    knights_lastname = str(input("What is the knights last name: "))
    knights_weapon = str(input("What is the knights weapon: "))
    knights_order = str(input("What is the knights order: "))
    
    knights_data[knights_number + 1] = {"Name":knights_name, "Lastname":knights_lastname, "Weapon":knights_weapon, "Order":knights_order}

    # Adds the knight information to the knights list (overall list)
    knights.append(knights_data)
    
## Call a knight and change their data
def change_data(knights, selected_knight):
    
    try:
        # Shows to the user what you want to update
        print("--- What would you like to update ---")
        print("1: Knight's name: " + knights[selected_knight][selected_knight + 1]['Name'])
        print("2: Knight's last name: " + knights[selected_knight][selected_knight + 1]['Lastname'])
        print("3: Knight's weapon: " + knights[selected_knight][selected_knight + 1]['Weapon'])
        print("4: Knight's order: " + knights[selected_knight][selected_knight + 1]['Order'])
        print()

        # The user needs to input a valid number
        selected_feature = int(input("Enter your option: "))

        if selected_feature == 1: 
            # The existing name is reassigned to the new name
            knights[selected_knight][selected_knight + 1]['Name'] = str(input("What is their new name: "))
            print("Your knight's new name is: " + knights[selected_knight][selected_knight + 1]['Name'])
            print()
            return selected_feature

        elif selected_feature == 2:                
            # The existing last name is reassigned to the new last name
            knights[selected_knight][selected_knight + 1]['Lastname'] = str(input("What is their new last name: "))
            print("Your knight's new last name is: " + knights[selected_knight][selected_knight + 1]['Lastname'])
            print()
            return selected_feature

        elif selected_feature == 3:                
            # The existing weapon is reassigned to the new weapon
            knights[selected_knight][selected_knight + 1]['Weapon'] = str(input("What is their new weapon: "))
            print("Your knight's new weapon is: " + knights[selected_knight][selected_knight + 1]['Weapon'])
            print()
            return selected_feature

        elif selected_feature == 4:                
            # The existing order is reassigned to the new order
            knights[selected_knight][selected_knight + 1]['Order'] = str(input("What is their new order: "))
            print("Your knight's new order is: " + knights[selected_knight][selected_knight + 1]['Order'])
            print()
            return selected_feature

        else:
          # if the number is not a valid option prints a message
            print("--- Please select a valid option ---")

    except:
        # if the unput is not a number a exception will be raised 
        print("--- Select a knight's number ---")
        change_data(knights)

## Prints all knights
def print_all_knights(knights):
    print("--- All your knights ---")

    # The knights will display if they knights list is not empty
    if len(knights) > 0:
        for index in range(len(knights)):
            name = knights[index][index + 1]['Name']
            lastname = knights[index][index + 1]['Lastname']
            weapon = knights[index][index + 1]['Weapon']
            order = knights[index][index + 1]['Order']
            print(f"{index + 1} - Knights's full name: {name} {lastname}, weapon: {weapon}, order: {order}")
    else:
        print("Wait... You have no knights! Instead have a number: " + str(random.randint(0, 100)))

## Shows the current knight and selected_option one
def select_knights(knights): 
    print("What 'knight' would you like to update?\n")

    # Displays all knights   
    print_all_knights(knights)

    # We need to know which knight we are talking about
    selected_knight = (int(input("\nSelect the knight's number: ")) - 1)
    print() # creates a blank line

    if selected_knight < len(knights): 
        change_data(knights, selected_knight)
    else:      
        print("--- Select a valid knight's number ---")
        print() # creates a blank line
        select_knights(knights)

## This is the menu and we make our collections here
def menu(knights):
    
    # Print the display options
    print("What do you want to do?")
    print() # creates a blank line
    print("1: Create a new knight")
    print("2: Update your knight")
    print("3: See all knights")
    print("0: Exit")
    print() # creates a blank line

    # Allows a selected_feature to be tested
    try:
        
        # Takes the users selected_feature option
        selected_option = int(input("Selection number: "))
        print() # creates a blank line

        # Create a new knight
        if selected_option == 1:
            create_knight(knights)
            print() # creates a blank line
            menu(knights)

        elif selected_option == 2:
            if len(knights) > 0:
                select_knights(knights)
                print() # creates a blank line
                menu(knights)

            else:
                print("--- First create a knight! ---")
                print() # creates a blank line
                menu(knights)

        elif selected_option == 3:
            print_all_knights(knights)
            print() # creates a blank line
            menu(knights)
                
        elif selected_option == 0:
            # Prints all the knigths
            print_all_knights(knights)            

    # Looking integer selected_feature
    except:
        print("--- Enter a valid option ---\n") 
        print() # creates a blank line
        menu(knights)

""" Setting the scene """
# Create a list
knights = []

# Run the program
menu(knights)