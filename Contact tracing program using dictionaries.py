# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# Display Menu
def menu():
    print("Menu: ")
    print("      1 -> Add an item. ")
    print("      2 -> Search. ")
    print("      3 -> Exit. ")
# Allow user to select and item in the menu
## User Input
## Check if valid


# Perform Selected Option 
## Option 1: Ask personal data for contact tracing // Full Name, Age, Address, Phone Number, Vaccinated, Positive or negative, Had covid before, Comorbidity

contact_tracing_dictionary = {}
def add_item():
    ### User Input
    #/// Full name
    while True:
        try:
            full_name = str(input("What is your full name?: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    #/// Age
    while True:
        try:
            age = int(input("What is your age?: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    #/// Address
    while True:
        try:
            address = input("What is your address?: ")
        except ValueError:
            print("Invalid input.")
            continue
        if not address.isalnum:
            print("Invalid input.")
        else:
            break
    #/// Phone number
    while True:
        try:
            phone_number = int(input("What is your phone number?: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    #/// Vaccine status
    while True:
        vaccine_status = str(input("Are you vaccinated? (Y/N): "))
        if vaccine_status.upper() not in ['Y', 'N']:
            print("Invalid input.")
            continue
        else:
            break
    #/// Covid status
    while True:
        covid_status = str(input("Are you currently postivie for covid? (Y/N): "))
        if covid_status.upper() not in ['Y', 'N']:
            print("Invalid input.")
            continue
        else:
            break
    #/// Previous Covid Status
    while True:
        previous_covid_status = str(input("Have you ever had covid? (Y/N): "))
        if previous_covid_status.upper() not in ['Y', 'N']:
            print("Invalid input.")
            continue
        else:
            break
    #/// Comorbidity
    while True:
        comorbidity = str(input("Do you have any comorbidity? (Y/N): "))
        if comorbidity.upper() not in ['Y', 'N']:
            print("Invalid input.")
            continue
        else:
            break
    ### Use dictionary to store info
    ### Use full name as key
    ### The value is another dictionary of personal information
    contact_tracing_dictionary = {
        full_name : {age, address, phone_number, vaccine_status, covid_status, previous_covid_status, comorbidity},
    }
    print(contact_tracing_dictionary)
## Option 2: Search, ask full name then display the record
def search_item():
    search_input = str(input("Enter full name of the record you're looking for: "))
    print(contact_tracing_dictionary.get(search_input))
## Option 3: Ask the user if they want to exit or retry
def exit():
    exit_input = str(input("Exit? (Y/N)"))
    while True:
        if exit_input.upper() == "N":
            main_menu()
        elif exit_input.upper() == "Y":
            break
        else:
            print("Invalid input.")
            exit()

def main_menu():
    menu()
    user_input = input("Enter the number of the function you want to use: ")
    while True:
            if user_input == "1":
                add_item()
            elif user_input == "2":
                search_item()
            elif user_input == "3":
                exit()
            else:
                print("Invalid input.")
                main_menu()
main_menu()