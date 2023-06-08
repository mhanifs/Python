# 1. Write a Python Program to Find the Factorial of a Number?


num = int(input("Enter a number: "))

fact = 1
for i in range(num, 0, -1):
    fact = fact * i

print("Factorial of {} is: {} ".format(num, fact))
# Enter a number: 7
# Factorial of 7 is: 5040

# 2. Write a Python Program to Display the multiplication Table?

num = int(input("Enter a number: "))
for i in range(1, 11):
        print("{} x {} x {}".format(num, i, num * i))
#
# Enter a number: 7
# 7 x 1 x 7
# 7 x 2 x 14
# 7 x 3 x 21
# 7 x 4 x 28
# 7 x 5 x 35
# 7 x 6 x 42
# 7 x 7 x 49
# 7 x 8 x 56
# 7 x 9 x 63
# 7 x 10 x 70

# 3. Write a Python Program to Print the Fibonacci sequence?

num = int(input("Enter a number: "))

n1, n2 = 0, 1

sum = 0

if num <= 0:
    print("Enter a positive integer")
else:
    for i in range(0, num):
        print(sum, end = " ")
        n1 = n2
        n2 = sum
        sum = n1 + n2

# Enter a number: 10
# 0 1 1 2 3 5 8 13 21 34

# 4. Write a Python Program to Check Armstrong Number?


def is_armstrong_number(num):
    number_str = str(num)
    power = len(number_str)
    sum_of_digits = 0

    for digit in number_str:
        sum_of_digits += int(digit) ** power


    if sum_of_digits == num:
        return True
    else:
        return False


num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

# Enter a number: 153
# 153 is an Armstrong number.

start = int(input("Enter start value of the range: "))
end = int(input("Enter end value of the range: "))

print("Armstrong numbers between range of {} and {} are".format(start, end))
for i in range(start, end):
    if is_armstrong_number(i):
        print(i, end = " ")

# Enter start value of the range: 150
# Enter end value of the range: 6000
# Armstrong numbers between range of 150 and 6000 are
# 153 370 371 407 1634 Enter a positive number:

# 6. Write a Python Program to Find the Sum of Natural Numbers?

num = int(input("Enter a positive number: "))

total_sum = 0
for i in range(1, num + 1):
    total_sum += i

print("Sum of {} natural number is {}".format(num, total_sum))

# Enter a positive number: 20
# Sum of 20 natural number is 210
