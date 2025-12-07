# 1. Write a program to read a text file and print each line with line numbers.
def print_file_with_line_numbers():
    try:
        # file = open('sunday.txt', 'r')
        # lines = file.read().split("\n")
        # for i in range(len(lines)):
        #     if lines[i] != "":
        #         print(f"line {i+1}: {lines[i]}")

        with open('sunday.txt', 'r') as file:
            for i, line in enumerate(file, 1):
                print(f"line {i}: {line.strip()}") # strip() removes the whitespaces

    except Exception as e:
        print(f"An error occurred: {e}")

print_file_with_line_numbers()

# --------------------------------------------------------------------------------------------------
# 2. Write a program to create a file and write five lines of text into it.
# --------------------------------------------------------------------------------------------------
def create_and_write_file():
    try:
        file = open('sunday.txt', 'w')
        for i in range(5):
            file.write(f"This is line {i+1}\n")
        file.close()
    except Exception as e:
        print(f"An error occurred: {e}")

create_and_write_file()

# --------------------------------------------------------------------------------------------------
# 3. Write a program to count the number of words in a given text file
# --------------------------------------------------------------------------------------------------
def count_words_in_file():
    try:
        file = open('sunday.txt', 'r')
        content = file.read().split() # splits the whole text into words
        print(content)
        print(len(content))
    except Exception as e:
        print(e)

count_words_in_file()

# --------------------------------------------------------------------------------------------------
# 4. Write a program that takes two numbers and handles the error if division by zero occurs.
# --------------------------------------------------------------------------------------------------
def division_by_zero():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    try:
        divide = num1 / num2
        print(divide)
    except ZeroDivisionError:
        print("Division by zero cannot be done.")

division_by_zero()

# --------------------------------------------------------------------------------------------------
# 5. Write a program that handles the error when trying to open a file that does not exist.
# --------------------------------------------------------------------------------------------------
def open_file_error():
    try:
        with open('sample.txt', 'r') as file:
            print(file)
    except FileNotFoundError:
        print("This file does not exits.")

open_file_error()

# --------------------------------------------------------------------------------------------------
# 6. Write a program that asks the user for an integer and handles invalid input.
# --------------------------------------------------------------------------------------------------
def user_invalid_input():
    try:
        num = int(input("Enter a number: "))
        print(num)
    except ValueError:
        print("Please enter a integer number...")    

user_invalid_input()

# --------------------------------------------------------------------------------------------------
# 7. Create a class with two attributes and print the values using objects
# --------------------------------------------------------------------------------------------------
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

obj1 = Person("abc", "def")
print("Person: ", obj1.name, obj1.surname )

# --------------------------------------------------------------------------------------------------
# 8. Create a class with methods to perform basic arithmetic operations and call them.
# --------------------------------------------------------------------------------------------------
class ArithmeticOperation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return(self.num1 + self.num2)
    def subs(self):
        return(self.num1 - self.num2)
    def divide(self):
        return(self.num1 / self.num2)
    def multiply(self):
        return(self.num1 * self.num2)

calc = ArithmeticOperation(2,8)
print(calc.add())
print(calc.subs())
print(calc.divide())
print(calc.multiply())

# --------------------------------------------------------------------------------------------------
# 9. Create a class with a constructor that initializes two attributes and displays them.
# --------------------------------------------------------------------------------------------------
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Name: ",self.name)
        print("Price: ",self.price)

car1 = Car("Toyota", 10000)
car1.display()

# --------------------------------------------------------------------------------------------------
# 10. Create a parent class and a child class where the child overrides one method.
# --------------------------------------------------------------------------------------------------
class Brand:
    def name(self):
        print("Car is of Toyota brand.")
    
class Car(Brand):
    def name(self):
        print("Car name is Corolla.")

brand = Brand()
car = Car()

brand.name()
car.name()