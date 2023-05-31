# Q1.  Write a Python program to print "Hello Python"?

print("Hello Python")
# Hello Python

# 2. Write a Python program to do arithmetical operations addition and division.?

a=20
b=5

# Addtition
Add= a+b

# Division

Div= a//b

print("Addition result: ", Add)
print("Division result:", Div)
# Addition result:  25
# Division result: 4

# 3. Write a Python program to find the area of a triangle?

height = 10
base = 5

area_of_triangle = height*base/2

print("Area of triangle: ", area_of_triangle)
# Area of triangle:  25.0

# 4. Write a Python program to swap two variables?
var1 = 245
var2 = 38

print("Before swap \n var1 = {} and var2 = {}" .format(var1, var2))

temp = var1
var1 = var2
var2 = temp
print('\nAfter swap:\nvar1 = {} and var2 = {}'.format(var1, var2))
# Before swap
#  var1 = 245 and var2 = 38

# After swap:
# var1 = 38 and var2 = 245

5. Write a Python program to generate a random number?

import random

number = random.randint(1, 10)
print("Random number is: ", number)
# Random number is:  10
