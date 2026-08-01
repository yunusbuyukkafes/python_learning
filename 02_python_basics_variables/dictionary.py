student = {
    "name": "Yunus",
    "surname": "Büyükkafes",
    "age": 21,
    "department": "Computer Engineering",
}
print(student)

print(student["name"])
print(student["age"])

# update
student["grade"] =91
print(student)

student["age"] = 22
print(student)

# delete
del student["department"]
print(student)

print(student.keys())
print(student.values())
print(student.items())