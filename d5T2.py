# Day 5. Make a simple login system without registration using functions
# Simple login system without registration using functions

def login_system():
    users = {
        "admin": "admin123",
        "user1": "password1",
        "user2": "password2",
    }

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print("Login successful!")
            return
        else:
            print("Invalid username or password. Please try again.\n")

login_system()


# ------------------------------------------------------------------------------------------------
# Day 5. Make a login system using registration using function
# Login system with registration using functions

def registration_system():
    # User list to store registered users
    users = {}

    # Function to register a new user
    def register():
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        users[username] = password # Storing username and password in dictionary
        print("Registration successful!\n")

    # Function to login an existing user
    def login():
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in users and users[username] == password:
                print("Login successful!")
                return
            else:
                print("\n Invalid username or password. Please try again.\n")
                print("If you don't have an account, please register first.\n")

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("\n Enter choice (1-3): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
            break
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")

registration_system()