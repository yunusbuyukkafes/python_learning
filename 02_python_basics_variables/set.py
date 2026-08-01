numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers_1={1, 2, 2, 3, 3}
print(numbers_1)

# list to set
list1 = [1, 2, 2, 3, 4, 5, 5,]
set1 = set(list1)
print(set1)

# add
numbers.add(6)
print(numbers)

# remove
numbers.remove(3)
print(numbers)

# example
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# union
print(a.union(b))

# intersection  
print(a.intersection(b))

# difference
print(a.difference(b))
