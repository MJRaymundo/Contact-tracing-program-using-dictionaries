# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# Display Menu
print("Menu: ")
print("      1 -> Add an item. ")
print("      2 -> Search. ")
print("      3 -> Exit. ")
# Allow user to select and item in the menu
## User Input
user_input = input("Enter the number of the function you want to use: ")
## Check if valid
# Perform Selected Option 
## Option 1: Ask personal data for contact tracing // Full Name, Age, Address, Phone Number, Vaccinated, Positive or negative, Had covid before, Comorbidity
### User Input
full_name = str(input("What is your full name?: "))
age = int(input("What is your age?: "))
address = input("What is your address?: ")
phone_number = int(input("What is your phone number?: "))
vaccine_status = str(input("Are you vaccinated? (Y/N): "))
covid_status = str(input("Are you currently positive for convid? (Y/N): "))
previous_covid_status = str(input("Have you been previously positive for covid? (Y/N): "))
comorbidity = str(input("Do you have any comorbidity (Y/N)?: "))
print(full_name, age, address, phone_number, vaccine_status, covid_status, previous_covid_status, comorbidity)
### Use dictionary to store info
### Use full name as key
### The value is another dictionary of personal information
## Option 2: Search, ask full name then display the record
## Option 3: Ask the user if they want to exit or retry