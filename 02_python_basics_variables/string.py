# string 
name = "Yunus"
surname = "Büyükkafes"
gender = "Male"
yas = 21
print("Name is", name)
print("Surname is", surname)
print("Gender is", gender)
print("Age is", yas)

# concatenation
id = name + " " + surname
print("ID is", id)

int_to_str = str(yas)
print (name +" "+ surname +" is " + int_to_str + " years old.")
print (f"{name} {surname} is {yas} years old.") # f string formatting

# string indexing
word = "Python"
print("First character is", word[0])

# string methods
text = "pytHon prograMming"
text_lower = text.lower()
text_upper = text.upper()
print("Lowercase:", text_lower)
print("Uppercase:", text_upper)

text_length = len(text)
print("Length of the text is", text_length)

text_replaced = text.replace("i", "I")
print("Replaced text is", text_replaced)
