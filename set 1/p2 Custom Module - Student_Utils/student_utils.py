# Martin Angel S. Padon
# Section: IV-BSIT B
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026

def calculate_average(grades):
    return sum(grades) / len(grades)


def get_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    return "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)