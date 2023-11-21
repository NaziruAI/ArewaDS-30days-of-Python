# importing inbuilt math method
import math

# function that take an argument of a number
def square_root(number):
    result = math.sqrt(number)
    return result

# Input number for which you want to find the square root
number = float(input("Enter a number: "))

if number < 0:
    print("Square root of negative numbers is undefined.")
else:
    sqrt = square_root(number)
    print(f"The square root of {number} is equal to: {sqrt}")
