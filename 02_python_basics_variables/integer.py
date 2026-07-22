# integer
age = 35 
print("your age is", age )

print()

# hesaplama
x=5
y=10
sum = x + y
print("sum is", sum)

difference = y - x
print("difference is", difference)

product = x * y
print("product is", product)

abstract = y / x
print("abstract is", abstract)

print()

# Example: Calculate total price of products
product1_price = 10
product2_price = 20
product3_price = 30
product1_quantity = 4
product2_quantity = 8
product3_quantity = 5

total_price = (product1_price * product1_quantity) + (product2_price * product2_quantity) + (product3_price * product3_quantity)
print("Total price of products is", total_price)

discount_percentage = int(input("Enter discount percentage: "))
discount_amount = (total_price * discount_percentage) / 100
final_price = total_price - discount_amount

print("Discount amount is", discount_amount)
print("Final price is", final_price)
