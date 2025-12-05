# Prepare a simple login and register system using File and function of usernames and passwords

import json

def register():
    username = input("Choose a username: ")
    file = open("day8.txt", "a+")
    users = file.read().split("\n") # get existing usernames and splitting them by new line

    for i in users:
        if i != "":
            dict_user = json.loads(i)  # load JSON string to dictionary
            if username in dict_user:
                print("Username already exists. Please choose a different username.\n")
                break
    else:
        password = input("Choose a password: ")
        dict_user = {username: password}  # changed to dictionary format (username: password)
        json_user = json.dumps(dict_user) # convert to JSON string to store in file

        file.write(json_user + "\n")
        file.close()
        print("Registration Successful \n")
    
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    file = open("day8.txt", "r")
    user = file.read().split("\n")
    file.close()
    for i in user:
        if i != "":
            user_dict = json.loads(i)
            if username in user_dict and user_dict[username] == password:
                print("Login Successful \n")
                break
    else:
        print("Invalid username or password. Please try again.\n")

while True:
    print("1. Register")
    print("2. Login") 
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")
    match choice:
        case '1':
            register()
        case '2':
            login()
        case '3':
            print("Exiting the system. Goodbye!")
            break
        case _:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

# # Prepare a login and register system using File and function of usernames password, balance and user should
# be able to check, deposit and withdraw money from his account

import json

# Register function to add username, password and balance to file
def register():
    username = input("Choose a username: ")
    file = open("day8t2.txt", "a+")
    users = file.read().split("\n") # get existing usernames and splitting them by new line

    for i in users:
        if i != "":
            user_dict = json.loads(i)  # load JSON string to dictionary
            if username in user_dict:
                print("Username already exists. Please choose a different username.\n")
                break
    else:
        password = input("Choose a password: ")
        balance = 0  # initial balance set to 0
        dict_user = {username: {"password": password, "balance": balance}}  # changed to dictionary format
        json_user = json.dumps(dict_user) # convert to JSON string to store in file

        file.write(json_user + "\n")
        file.close()
        print("Registration Successful \n")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    file = open("day8t2.txt", "r")
    userlist = file.read().split("\n")
    file.close()

    updated_userlist = []  # to store all user data after updates

    for i in userlist:
        if i != "":
            user_dict = json.loads(i)
            updated_userlist.append(user_dict)  # add existing user data to the list

            if username in user_dict and user_dict[username]["password"] == password:
                print("Login Successful \n")

                while True:
                    print("1.Check Balance")
                    print("2.Deposit Money")
                    print("3.Withdraw Money")
                    print("4.Logout")

                    choice = input("\nEnter choice (1-4): ")
                    match choice:
                        case '1':
                            print(f"Your balance is: ${user_dict[username]['balance']}\n")
                        case '2':
                            amount = float(input("Enter amount to deposit: "))
                            user_dict[username]['balance'] += amount
                            print("updated user:", user_dict)
                            print(f"${amount} deposited successfully. New balance is: ${user_dict[username]['balance']}\n")
                        case '3':
                            amount = float(input("Enter amount to withdraw: "))
                            if 0 < amount <= user_dict[username]['balance']:
                                user_dict[username]['balance'] -= amount
                                print(f"${amount} withdrawn successfully. New balance is: ${user_dict[username]['balance']}\n")
                            else:
                                print("Insufficient balance.\n")
                        case '4':
                            print("Logging out...\n")
                            break
                        case _:
                            print("Invalid choice.\n")
    else:
        print("Invalid username or password. Please try again.\n")
    
    print("updated_userlist", updated_userlist)
    print("userlist: ", userlist)

    # Overwriting the file with updated user data (can't update/modify existing data in file directly)
    file = open("day8t2.txt", "w")
    for user in updated_userlist:
        json_user = json.dumps(user)
        file.write(json_user + "\n")
    file.close()
    print("User data updated in file.")


while True:
    print("1. Register")
    print("2. Login") 
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")
    match choice:
        case '1':
            register()
        case '2':
            login()
        case '3':
            print("Exiting the system. Goodbye!")
            break
        case _:
            print("Invalid choice.\n")