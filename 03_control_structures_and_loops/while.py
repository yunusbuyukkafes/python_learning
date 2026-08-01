i=0
while i < 5:
    print(i)
    i += 1
print (f"i = {i}")

counter = 0
while counter < 3:
    print("Merhaba")
    counter += 1

i=0
while i < 10:
    if i % 2 == 0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")
    i += 1

input1 = ""
while input1 != "q":
    input1 = input("Enter a character (q to quit): ")
    print(f"You entered: {input1}")