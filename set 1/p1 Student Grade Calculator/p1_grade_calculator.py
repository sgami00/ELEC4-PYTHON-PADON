# Martin Angel S. Padon
# Section: IV-BSIT B
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026

grades = []


def enter_grades():
    grades.clear()

    while True:
        try:
            count = int(input("How many grades will you enter? "))

            if count > 0:
                break
            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid grade. Please enter a number.")


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    if calculate_average(grades) >= 75:
        return "PASSED"
    return "FAILED"


def display_results():
    if not grades:
        print("No grades available. Enter grades first.")
        return

    print("\n===== STUDENT GRADE RESULTS =====")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest Grade: {get_highest(grades)}")
    print(f"Lowest Grade: {get_lowest(grades)}")
    print(f"Status: {get_status(grades)}")


while True:
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("1. Enter Grades")
    print("2. View Results")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        enter_grades()

    elif choice == "2":
        display_results()

    elif choice == "3":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice. Please try again.")


# Local variables exist inside their respective functions.
# For example, count and grade are local variables in enter_grades().
# The grades list is a global variable because it is declared outside
# the functions and can be accessed by different parts of the program.
# Local variables are only accessible within their function.