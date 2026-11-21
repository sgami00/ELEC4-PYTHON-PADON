# Martin Angel S. Padon
# Section: IV-BSIT B
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026

students = []


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    for student in students:
        if student.lower() == name.lower():
            print("Student already exists.")
            return

    students.append(name)
    print("Student successfully added!")


def remove_student():
    name = input("Enter name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print("Student removed successfully!")
            return

    print("Student not found.")


def search_student():
    keyword = input("Enter name to search: ").strip().lower()

    matches = [
        student for student in students
        if keyword in student.lower()
    ]

    if matches:
        print("\nSearch Results:")
        for student in matches:
            print(student)
    else:
        print("No matching student found.")


def display_students():
    if not students:
        print("No student records available.")
        return

    unique_students = sorted(set(students), key=str.lower)

    print("\n===== STUDENT LIST =====")

    for number, student in enumerate(unique_students, start=1):
        print(f"{number}. {student}")

    print("Total Students:", len(unique_students))


while True:
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        remove_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Program closed.")
        break

    else:
        print("Invalid selection.")


# A list stores student names and allows adding and removing entries.
# A set stores only unique values, so it can help prevent duplicates.
# This program uses a list for the main student records.
# It uses a set when displaying the unique student names.