coordinate = (10, 20)
colors = ("red", "green", "blue", "yellow")
print(coordinate[0]) 

# list vs tuple
list_1 = [1, 2, 3] 
tup = (1, 2, 3)

list_1[0] = 10
print(list_1)

# tup[0] = 10 # TypeError: 'tuple' object does not support item assignment
# print(tup)

t=(10, 20, 30, 40, 50)
print(t)
print(t[0]) # 10
print(t[1:4]) # (20, 30, 40)

x = (3) # int or tuple
print(type(x)) # <class 'int'>
y = (3,) 
print(type(y)) # <class 'tuple'>

# tuple unpacking
numbers = (10, 20,)
a, b = numbers
print(a) 
print(b) 

# tuple methods
t = (10, 20, 20, 30, 40, 50)
print(t.count(20)) 
print(t.count(30))

print(t.index(30))
