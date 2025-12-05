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


# ------------------------------------------------------------------------------------------------
# Day 5. Print a multiplication table of the number that is input by the user

# Multiplication table program
num = int(input("\n Enter a number to print its multiplication table: "))
print(f"Multiplication table for {num}: ")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# ------------------------------------------------------------------------------------------------
#  Day 5. Check if the given number is even or odd

# Even or Odd checker
num = int(input("\n Enter a number to check if it is even or odd: "))

if num% 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")


# ------------------------------------------------------------------------------------------------
# Day 5. Check if a given number is palindrome or not

# Palindrome checker
num = input("\n Enter a number to check if it is a palindrome: ")

if num == num[::-1]:
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is not a Palindrome.")


# ------------------------------------------------------------------------------------------------
# Day 5. Print all the even numbers in a list of numbers
# Even numbers in a list

numbers = [10, 23, 45, 66, 78, 89, 90, 12, 34, 56]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("\n Even numbers in the list are:", even_numbers)