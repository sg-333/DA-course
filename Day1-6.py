# -------------------------------------SIMPLE CALCULATOR--------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Day 1. SIMPLE CALCULATOR APP by assigning values

# Assigning two values 
num1 = 10
num2 = 2

# Performing arithmetic operations
add = num1 + num2
sub = num1 - num2
multiply = num1 * num2
divide = num1 / num2
floorD = num1 // num2
mod = num1 % num2
exp = num1 ** num2

print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", multiply) 
print("Division: ", divide)
print("Floor Division: ", floorD)
print("Modulus: ", mod)
print("Exponentiation: ", exp)


# ----------------------------------------CALCULATOR APP----------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Day 1. SIMPLE CALCULATOR APP by taking values from user

# Taking two values from user
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    # Performing arithmetic operations
    add = num1 + num2
    sub = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2
    floorD = num1 // num2
    mod = num1 % num2
    exp = num1 ** num2
    
    print("Addition: ", add)
    print("Subtraction: ", sub)
    print("Multiplication: ", multiply) 
    print("Division: ", divide)
    print("Floor Division: ", floorD)
    print("Modulus: ", mod)
    print("Exponentiation: ", exp)

except Exception as e:
    print(e)

# --------------------------------------------------
# Day 2. Update the above calculator program using IF…ELSE

try:
    print("Select operation:")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("5. Floor Division")
    print ("6. Modulus")
    print ("7. Exponentiation") 

    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    if choice == '1':
        num = num1 + num2
        print("Addition is: ", num)
    elif choice == '2':
        num = num1 - num2
        print("Subtraction is: ", num)
    elif choice == '3':
        num = num1 * num2
        print("Multiplication is: ", num) 
    elif choice == '4':
        num = num1 / num2
        print("Division is: ", num)
    elif choice == '5':
        num = num1 // num2
        print("Floor Division is: ", num)
    elif choice == '6':
        num = num1 % num2
        print("Modulus is: ", num)
    elif choice == '7':
        num = num1 ** num2
        print("Exponentiation is: ", num)
    else:
        print("Invalid input")

except Exception as e:
    print(e)
# ------------------------------------------------
# Day 3. Update the above Calculator program using match
try:
    match choice:
        case '1':
            num = num1 + num2
            print("Addition is: ", num)
        case '2':
            num = num1 - num2
            print("Subtraction is: ", num)
        case '3':
            num = num1 * num2
            print("Multiplication is: ", num) 
        case '4':
            num = num1 / num2
            print("Division is: ", num)
        case '5':
            num = num1 // num2
            print("Floor Division is: ", num)
        case '6':
            num = num1 % num2
            print("Modulus is: ", num)
        case '7':
            num = num1 ** num2
            print("Exponentiation is: ", num)
        case _:
            print("Invalid input")    
except Exception as e:
    print(e)

# -------------------------------------------LIST, DICTIONARY-----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Day 2. Create a list of usernames
# Input a username from the user. Check if the username is present in the list or not

usernames = ["alice", "bob", "charlie", "david", "eve"]
name = input("Enter a username: ")
if name in usernames:
    print("Username found!")
else:
    print("Username not found.")

# ----------------------------------------------
# Day 2. Create a dictionary of usernames and passwords, extract all the usernames from the dictionary and 	
# input username from the user and check if the username is present in the extracted list of 	usernames

user = {"alice": "password123",
        "bob": "qwerty",
        "charlie": "letmein",
        "david": "123456",
        "eve": "trustno1"
}

# Extracting usernames
usernames = list(user.keys())
print("Extracted Usernames: ", usernames)
name = input("Enter a username: ")

if name in usernames:
    print("Username found!")
else:
    print("Username not found.")

# Update the login dictationary program using IF ELSE
username = input("Enter your username: ")
password = input("Enter your password: ")
if username in user:
    if user[username] == password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

# -----------------------------------------------GREATEST NUMBER--------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Day 2. Find the greatest and smallest number among three numbers using IF…ELSE and logical operators
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    if (num1 >= num2) and (num1 >= num3):
        print("Greatest number is:", num1)
    elif (num2 >= num1) and (num2 >= num3):
        print("Greatest number is:", num2)
    else:
        print("Greatest number is:", num3)
except Exception as e:
    print(e)


# -----------------------------------------------------LOOP-------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Day 3. Update all the programs that we have done using the loop. You can use any type of loop

# 1. Calculator app using loop
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Floor Division")
        print("7. Exponentiation")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == "1":
            print("Addition:", num1 + num2)
        elif choice == "2":
            print("Subtraction:", num1 - num2)
        elif choice == "3":
            print("Multiplication:", num1 * num2)
        elif choice == "4":
            print("Division:", num1 / num2)
        elif choice == "5":
            print("Modulus:", num1 % num2)
        elif choice == "6":
            print("Floor Division:", num1 // num2)
        elif choice == "7":
            print("Exponentiation:", num1 ** num2)
        elif choice == "8":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid option! \n")
    except Exception as e:
        print(e)

# --------------------------------------------------------------
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


# ---------------------------------------------------LOGIN SYSTEM-------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Day 3. Make a accounting system where a user logins and he should be able to check the balance, 
# add balance and withdraw balance. Use dictionary, IF…ELSE and loop if needed

# Accounting system with login and balance management
# List of users with passwords and balances in dictionary
users = {
    "alice": {"password": "password123", "balance": 1000},
    "bob": {"password": "qwerty", "balance": 1500},
    "charlie": {"password": "letmein", "balance": 2000},
}
# Login process
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


# ----------------------------------------------FUNCTIONS, MULTIPLICATION TABLE, ODD/EVEN-------------------------------
# ----------------------------------------------------PALINDROME, LIST(EVEN NO.)----------------------------------------
# Day 5. Make a calculator program using Python functions and loop

# Calculator program with functions and loop
# Calc functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
def floorDivide(x, y):
    if y != 0:
        return x // y
    else:
        return "Error! Division by zero."
def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error! Division by zero."
def exponent(x, y):
    return x ** y

# Loop for calculator
while True:
    print("\n Select operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Floor Divide")
    print("6. Modulus")
    print("7. Exponent")
    print("8. Exit")

    choice = input("\n Enter choice (1-8): ")

    try:
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            match choice:
                case '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                case '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                case '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                case '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                case '5':
                    print(f"{num1} // {num2} = {floorDivide(num1, num2)}")
                case '6':
                    print(f"{num1} % {num2} = {modulus(num1, num2)}")
                case '7':
                    print(f"{num1} ** {num2} = {exponent(num1, num2)}")
                case _:
                    print("Invalid input")

        elif choice == '8':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid Input")
    except Exception as e:
        print(e)

# ------------------------------------------------------------------------------
# Day 5. Print a multiplication table of the number that is input by the user

# Multiplication table program
try:
    num = int(input("\n Enter a number to print its multiplication table: "))
    print(f"Multiplication table for {num}: ")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except Exception as e:
    print(e)

# ------------------------------------------------------------------------------
#  Day 5. Check if the given number is even or odd

# Even or Odd checker
try:
    num = int(input("\nEnter a number to check if it is even or odd: "))

    if num% 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")
except Exception as e:
    print(e)


# ------------------------------------------------------------------------------
# Day 5. Check if a given number is palindrome or not

# Palindrome checker
try:
    num = input("\n Enter a number to check if it is a palindrome: ")

    if num == num[::-1]:
        print(f"{num} is a Palindrome.")
    else:
        print(f"{num} is not a Palindrome.")
except Exception as e:
    print(e)

# ------------------------------------------------------------------------------
# Day 5. Print all the even numbers in a list of numbers
# Even numbers in a list
try:
    numbers = [10, 23, 45, 66, 78, 89, 90, 12, 34, 56]
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    print("\nEven numbers in the list are:", even_numbers)
except Exception as e:
    print(e)

# ------------------------------------------------LOGIN SYSTEM ONLY USING FUNCTION--------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
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


# ---------------------------------------------LOGIN, REGISTRATION SYSTEM USING FUNCTION--------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Day 5. Make a login system using registration using function
# Login system with registration using functions

def system():
    # To store registered users
    users = {}

    # Function to register a new user
    def register():
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        users[username] = password # Storing username and password in dictionary
        print("\nRegistration successful!\n")
        print("userlist: \n", users)

    # Function to login an existing user
    def login():
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in users and users[username] == password:
                print("Login successful!")
                return
            else:
                print("\nInvalid username or password. Please try again.")
                print("If you don't have an account, please register first.\n")

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("\nEnter choice (1-3): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
            break
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice.\n")

system()
