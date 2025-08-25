"""

Write a Python program that asks the user for a positive integer n, then prints all numbers from 1 to n, one per line, using a while loop

"""

number = int(input("Please insert a positive integer: "))
counter = 1

while counter <= number:
    print(f"Current value: {counter}")
    counter += 1
