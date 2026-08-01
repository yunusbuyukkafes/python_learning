numbers = [10, 20, 30, 40, 50]
for number in numbers:  
    print(number+5)

#range 
for i in range(5):
    print(i)

# example of calculating the sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("The sum of numbers from 1 to 10 is:", total)

# for and if statement
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# string iteration
word = "Yunus"
for letter in word:
    print(letter)