# Martin Angel S. Padon
# Section: IV-BSIT B
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026

def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation completed.")


def open_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File does not exist.")

    except PermissionError:
        print("Error: You do not have permission to open this file.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(content)

    finally:
        print("File operation completed.")


while True:
    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Division")
    print("2. Open File")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        divide_numbers()

    elif choice == "2":
        open_file()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid menu selection. Please try again.")