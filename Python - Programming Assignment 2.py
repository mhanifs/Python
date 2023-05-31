# 1. Write a Python program to convert kilometers to miles?

km = 10
miles = km/1.6
print(" {} km is equivalent to {} miles" .format(km, miles))
# 10 km is equivalent to 6.25 miles

# 2.Write a Python program to convert Celsius to Fahrenheit?

celsius= 35
fahrenheit= (9*celsius/5)+ 32
print("{} Celsius = {} Fahrenheit".format(celsius, fahrenheit))
# 35 Celsius = 95.0 Fahrenheit

# 3. Write a Python program to display calendar?

import calendar

year= 2023
month= 12
print(calendar.calendar(year))

# 4. Write a Python program to solve quadratic equation?


import math
print("ax^2 + bx^1 + c = 0")
print("Enter the coeff a, b and constant c")

a = int(input(("Enter the coeff a: ")))
b = int(input(("Enter the coeff b: ")))
c = int(input(("Enter the constant c: ")))

d = (b**2) - (4*a*c)

root1 = ((-b)+(math.sqrt(d))) / (2*a)
root2 = ((-b)-(math.sqrt(d))) / (2*a)

print('\nFor quad eq. {}x^2 + ({})x^1 + {}'.format(a,b,c))
print('The roots are: {} and {}'.format(root1, root2))
# For quad eq. 10x^2 + (15)x^1 + 2
# The solutions are: -0.14792027106038522 and -1.3520797289396147


# 5. Write a Python program to swap two variables without temp variable?

var1= 7
var2= 5

print("Variables before swap:\nvar1= {} and var2= {}". format (var1, var2))

var2= var1 + var2
var1= var2 - var1
var2= var2 - var1

print("Variables after swap:\nvar1= {} and var2= {}". format (var1, var2))

# Variables before swap:
# var1= 7 and var2= 5
# Variables after swap:
# var1= 5 and var2= 7
