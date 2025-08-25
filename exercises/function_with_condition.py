"""

Write a Python function that takes an integer as input and returns whether the number is "Even" or "Odd".
Ask the user to input a number and call the function to display the result.

"""

# Define the function
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Ask the user for input
user_number = int(input("Insert a number: "))

# Call the function and print the result
result = even_or_odd(user_number)
print(f"The number {user_number} is {result}.")