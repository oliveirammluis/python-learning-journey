"""

If / Else

Ask the user to enter their age.

If the age is greater than or equal to 18, print:
👉 "You are an adult."

Otherwise, print:
👉 "You are a minor."

"""

age = int(input("Please enter your age: "))

if age < 18:
    print("You are a minor.")
else: 
    print("You are an adult.")
