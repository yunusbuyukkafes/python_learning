"""
Get midterm and final exam grades from the user
- Calculate average
- Determine letter grade
- Display the result on screen
"""

# Grade calculation system
def calculate_average(midterm: float, final: float) -> float:
    """
    Calculates average: Midterm 40%, Final 60%.
    """
    average = midterm * 0.4 + final * 0.6
    return average

def determine_letter_grade(average: float) -> str:
    """
    Returns letter grade based on the average value.
    """
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

def print_result(name: str, average: float, letter_grade: str):
    """
    Prints the result to the console.
    """
    print("-------RESULT-------")
    print("Student Name: " + name)
    print("Average: " + str(average))
    print("Letter Grade: " + letter_grade)


# Program flow
name = input("Student name: ")
midterm = float(input("Midterm grade: "))
final = float(input("Final grade: "))

average = calculate_average(midterm=midterm, final=final)
letter_grade = determine_letter_grade(average=average)

print_result(name=name, average=average, letter_grade=letter_grade)