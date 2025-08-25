"""

Write a Python program that asks the user to input their grade (0–100).

If the grade is 90 or above, print "Excellent".

If the grade is between 70 and 89, print "Good".

If the grade is between 50 and 69, print "Pass".

Otherwise, print "Fail".

"""

grade = int(input("Please insert your grade: "))

if grade >= 90:
    print("Excellent")
elif grade >= 70:
    print("Good")
elif grade >= 50:
    print("Pass")
else:
    print("Fail")