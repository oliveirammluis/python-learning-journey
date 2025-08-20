# Integer Input Validator

while True:
    try:
        num = int(input("Enter an integer number: "))
        break  # exit the loop if the conversion is successful
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

print("You entered:", num)
