# local variables
def test ():
    x = 10
    print(f"x : {x}")

test() 

# print(f"x : {x}") # NameError: name 'x' is not defined

# global variables
x = 15
def test2 ():
    print(f"x : {x}")

test2()

# same name variables
x=11
def test3 ():
    x = 16
    print(f"x : {x}")

test3()
print(f"x : {x}") 

# global keyword
x = 18
def test4 ():
    global x
    x = 20

test4()
print(f"x : {x}")
