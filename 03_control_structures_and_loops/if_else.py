numbers = 19
if numbers > 0:
    print("The number is positive.")
else:
    print("The number is negative or zero.")

grade = 58
if grade >= 70:
    print("The student has passed.")
elif grade >= 60:
    print("The student has passed with a conditional pass.")
else:
    print("The student has failed.")

age = 25
student = True
if age <= 18 and student:
    print("Student discount applied!")

vegetables = ["carrot", "broccoli", "spinach"]
if "carrot" in vegetables:
    print("Carrot is available.")
else:
    print("Carrot is not available.")

product=input("Enter a vegetable name: ")
if product in vegetables:
    print(f"{product} is available.")
else:
    print(f"{product} is not available.")