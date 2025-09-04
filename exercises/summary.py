# --- PYTHON SUMMARY SCRIPT ---

# Variables
name = "Luis"
age = 18
active = True
balance = 150.50

print(f"\nVariables # Name: {name}, Age: {age}, Active: {active}, Balance: {balance}")

# Math operators
sum_result = age + 5
multiplication = age * 2
remainder = age % 4
print("\nMath operators # Sum:", sum_result, "Multiplication:", multiplication, "Remainder:", remainder)

# Logical operators
print("\nIs adult?", age >= 18 and active)

# Lists
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print("\nFruit list:", fruits)

# Dictionaries
user = {
    "name": "John",
    "email": "john@email.com",
    "age": 30
}
print("\nUser:", user["name"], "-", user["age"], "years old")

# Conditional structures
if balance > 100:
    print("\nYou have enough money 😎")
elif balance == 100:
    print("\nYou are at the limit...")
else:
    print("\nYou need to recharge your account!")

# For loop
print("\nAvailable fruits:")
for fruit in fruits:
    print("\n-", fruit)

# While loop
counter = 3
while counter > 0:
    print("Countdown:", counter)
    counter -= 1

# Functions
def greeting(name):
    return f"Hello, {name}! Welcome to Summary Python Exercise"

print(greeting("John"))

# Try/Except (error handling)
try:
    number = int("abc")  # this will throw an error
except ValueError:
    print("Error: invalid value when converting to integer.")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# User input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Nice to meet you, {user_name}! In 5 years you will be {user_age + 5}.")
