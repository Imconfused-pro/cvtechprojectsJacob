import csv
import json
while True:
    header = ["first", "last", "phone number"]

    print("""
    Please pick one prompt:
    1. Append CSV file
    2. View CSV file
    3. Convert CSV file into JSON
    Q. quit
        """)

    users_Option = input("Please pick one prompt: ")

    if users_Option == "q":
        print("Exiting the program. Goodbye!")
        break

    elif users_Option == "1":
        first_Name = input("Enter your first name: ")
        last_Name = input("Enter your last name: ")
        phone_Number = input("Enter your phone number: ")
        full_information = [first_Name, last_Name, phone_Number]

        with open("employees.csv", "a", newline=' ') as file: # newline = ' ' for correct row spacing
            csvreader = csv.writer(file)
            csvreader.writerow(full_information)
            reader = csv.DictReader(file)
            data = [row for row in csvreader]


        print("Please view employees.csv file to see results! :)))")

    elif users_Option == "2":
        with open("NamesandNumbers.csv", "r") as file:
            csvreader = csv.reader(file)
            for line in file:
                print(line.strip()) # .strip() helps clean up each line by removing any extra spaces
     
    elif users_Option == "3":
        print("Converting the CSV file to JSON and viewing...")
        
            
                    

    else:
        print("Invalid answer, please try again...")