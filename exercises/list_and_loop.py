"""
List and Loop

Write a Python program that:

Creates a list of at least 5 of your favorite fruits (or any items you like).

Loops through the list and prints each item, prefixed by "I like:".
"""

fruits = ["apple", "banana", "cherry", "melon"]

for i in range(len(fruits)):
    print(f"I like: {fruits[i]}")



for index, fruit in enumerate(fruits, start=1):
    print(f"I love: {index} - {fruit}")