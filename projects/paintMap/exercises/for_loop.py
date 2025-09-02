"""

Write a Python program that asks the user for a positive integer n, then prints all numbers from 1 to n, one per line, prefixed by:

"""

number = int(input("Please insert a positive integer: "))

for i in range(1, number + 1):
    print(f"Current value: {i}")