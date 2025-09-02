"""

Write a Python program that:

Asks the user to enter a list of numbers (comma-separated).

Converts the input into a list of integers.

Prints each number along with whether it is even or odd.

Calculates and prints the sum of all numbers.

Finds and prints the largest and smallest number.

Prints the numbers in ascending order.

"""

user_input = input("Please insert a list of numbers (comma-separated): ")
numbers = [int(x) for x in user_input.split(",")]

# Sum
total = sum(numbers)
print(f"The sum of all numbers is: {total}")

# Even or Odd
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Largest and Smallest
print(f"The largest number is: {max(numbers)}")
print(f"The smallest number is: {min(numbers)}")

# Ascending order
numbers.sort()
print(f"Numbers in ascending order: {numbers}")
