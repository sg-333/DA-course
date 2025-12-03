# Prepare a simple login and register system using File and function only of usernames

def register():
    username = input("Choose a username: ")
    file = open("day7.txt", "a")
    file.write(username + "\n")
    file.close()
    print("Registration Successful \n")

def login():
    username = input("Enter your username: ")
    file = open("day7.txt", "r")
    user = file.read().split("\n")
    file.close()
    if username in user:
        print("Login Successful \n")
    else:
        print("Login Failed \n")

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
