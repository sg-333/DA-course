# 2. Make a accounting system where a user logins and he should be able to check the balance, 
# add balance and withdraw balance. Use dictionary, IF…ELSE and loop if needed

# Accounting system with login and balance management
users = {
    "alice": {"password": "password123", "balance": 1000},
    "bob": {"password": "qwerty", "balance": 1500},
    "charlie": {"password": "letmein", "balance": 2000},
}
# Login process
# Keep asking until correct
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users:
        if users[username]["password"] == password: # Checking password for user
            print("Login successful!")
            break
        else:
            print("Incorrect password. Try again. \n")
    else:
        print("Username not found. Try again. \n") 

# Balance management
while True:
    print("\nSelect an option:")
    print("1. Check Balance")
    print("2. Add Balance")
    print("3. Withdraw Balance")
    print("4. Exit")
    # Asking user choice
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${users[username]['balance']}") # Display balance

    # Add balance
    elif choice == "2":
        amount = float(input("Enter amount to add: $"))
        if amount > 0:
            users[username]["balance"] += amount # Adding amount to balance
            print(f"${amount} added successfully. New balance is: ${users[username]['balance']}") 
        else:
            print("Invalid amount. Please enter a positive number.")

    # Withdraw balance
    elif choice == "3":
        amount = float(input("Enter amount to add: $"))
        if 0 < amount <= users[username]["balance"]:
            users[username]["balance"] -= amount # Subtracting amount from balance
            print(f"${amount} withdrawn successfully. New balance is: ${users[username]['balance']}")
        else:
            print("Invalid amount. Please enter a positive number within your balance.")
        
    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break

