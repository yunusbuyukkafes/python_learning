# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(10):
    if i == 5:
        continue
    print(i)

# pass
for i in range(3):
    if i == 1:
        pass
    else:
        print(i)

# nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

