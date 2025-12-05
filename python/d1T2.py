# SIMPLE CALCULATOR APP by taking values froom user

# Taking two values from user
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
# ---------------------------------------------------------------------------------------------------
# Day 2 Update the calculator program using IF…ELSE
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

# ---------------------------------------------------------------------------------------------------
# Day3 Update the Calculator program using match
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