# Day 3. Update all the programs that we have done using the loop. You can use any type of loop

# 1. Calculator app using loop
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operations = {
    "1": ("Addition", num1 + num2),
    "2": ("Subtraction", num1 - num2),
    "3": ("Multiplication", num1 * num2),
    "4": ("Division", num1 / num2),
    "5": ("Modulus", num1 % num2),
    "6": ("Floor Division", num1 // num2),
    "7": ("Exponentiation", num1 ** num2)
}
# Displaying the operations using a loop
print("Select operation:")
for key in operations:
    name = operations[key][0] # Getting operation name
    print(f"{key}. {name}")

choice = input("Enter choice (1-7): ")

if choice in operations:
    operation_name, result = operations[choice] # Getting operation name and result eg: (operation_name=Addition, result=15)
    print(f"{operation_name} is: {result}")
else:
    print("Invalid input")


# -----------------------------------------------------------------------------------
# Day 3. Dictionary of usernames and passwords with loop
# List of users
user = {"alice": "password123",
        "bob": "qwerty",
        "charlie": "letmein",
        "david": "123456",
}

# Keep asking for username and password until correct
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user:
        if user[username] == password: # Checking password for user
            print("Login successful!")
            break
        else:
            print("Incorrect password. Try again. \n")
    else:
        print("Username not found. Try again. \n")