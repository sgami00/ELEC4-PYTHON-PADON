# Martin Angel S. Padon
# Section: IV-BSIT B
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026

import student_utils
from datetime import datetime

print("===== STUDENT GRADE REPORT =====")

grades = []

while True:
    try:
        count = int(input("Enter number of grades: "))

        if count > 0:
            break

        print("Enter a number greater than zero.")

    except ValueError:
        print("Invalid input.")

for i in range(count):
    while True:
        try:
            grade = float(input(f"Enter grade {i + 1}: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break

            print("Grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

average = student_utils.calculate_average(grades)
highest = student_utils.get_highest(grades)

lowest = student_utils.get_lowest(grades)
status = student_utils.get_status(grades)

print("\n===== RESULTS =====")
print("Average:", round(average, 2))
print("Highest:", highest)
print("Lowest:", lowest)
print("Status:", status)

print("Report Date:", datetime.now().strftime("%B %d, %Y %I:%M %p"))