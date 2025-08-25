"""

Write a Python program that creates a dictionary with the names of 5 students as keys and their grades as values.

Then, print each student's name along with their grade. Finally, ask the user for a student name and print that student's grade. If the student is not in the dictionary, print "Student not found".

"""

grades = {
    "Alice": 85,
    "Barbara": 92,
    "Carlos": 76,
    "Diogo": 90,
    "Eduardo": 67
}

print(grades)

student_name = input("Enter a student name: ")

if student_name in grades:
    print(f"{student_name}'s grade is: {grades[student_name]}")
else:
    print("Student not found")