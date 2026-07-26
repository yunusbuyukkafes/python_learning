numbers = [1, 2, 3, 4, 5]
colors = ["red", "green", "blue", "yellow"]
mixed = [1, "apple", 3.14, True]

print(mixed)

#index
print(colors[0]) # "red"
print(colors[3]) # "yellow"
print (colors[-1]) # "yellow"
print (colors[-2]) # "blue"

# length
print(len(numbers)) # 5

# slicing
print(numbers[1:4]) # [2, 3, 4]
print(numbers[:3]) # [1, 2, 3]
print(numbers[2:]) # [3, 4, 5]

# append
numbers.append(6)
print(numbers) 

numbers.insert(2, 100)
print(numbers) 

numbers.remove(100)
print(numbers) 

numbers.pop() # removes the last element
print(numbers) 

numbers.pop(1) # removes the element at index 1
print(numbers) 

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

numbers[1] = 200
print(numbers)

numbers.clear()
print(numbers)
