# defination of a function
def greet():
    print("Hello")
greet()

def greet_user(name):
    print(f"Hello {name}")
greet_user("Yunus")

def greet_user_with_age(name, age):
    print(f"Hello {name}, you are {age} years old")
greet_user_with_age("Yunus", 21)

# return 
def sum (a, b):
    result = a + b
    print(f"result : {result}")
    return result
the_sum = sum (5, 4)
print(f"the sum : {the_sum}")

def calculate(a,b):
    sum = a + b
    product = a * b
    return sum, product
result_sum, result_product = calculate(5, 4)
print(f"result sum : {result_sum}")
print(f"result product : {result_product}")

def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old")

greet("Yunus")
greet("Yunus", 21)

def greet(name, age, job, c, lr, epooch):
    print(name, age, job, c, lr, epooch)
    
greet("Yunus", 21, "Software Engineer", c=0.1, lr=0.001, epooch=1000)

def calculate(a: int, b: int) -> int:
    return a + b
print(calculate(3,7))

def calculate(x):
    return x ** 2

def calculate2(x):
    return calculate(x) ** 2
print(calculate2(5))
