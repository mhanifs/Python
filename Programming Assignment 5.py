# Assignment - 5


# 1. Write a Python Program to Find LCM?

def find_lCM(n1, n2):
    if n1>n2:
        higher = n1
    else:
        higher = n2
    value = higher
    while True:
        if higher%n1==0 and higher%n2==0:
            print("LCM of", n1, "and", n2, "is", higher)
            break
        else:
            higher = higher+value


n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

find_lCM(n1,n2)

# Enter the first number:24
# Enter the second number:36
# LCM of 24 and 36 is 72

# 2. Write a Python Program to Find HCF?

def find_hcf(n1, n2):
    low = a if a < b else b
    for i in range(1, low + 1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return (hcf)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
find_hcf(a, b)
print("HCF for {} and {}".format(a, b), "is", find_hcf(a, b))

# Enter the first number:10
# Enter the second number:20
# HCF for 10 and 20 is 10


# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

num = int(input("Enter a number to convert into Binary, Octal & Hexadecimal: "))

print("Converted values of ", num, "is as follow")
print ("Binary:      ", bin(num))
print ("Octal:       ", oct(num))
print ("Hexadecimal: ", hex(num))

# Enter a number to convert into Binary, Octal & Hexadecimal: 15
# Converted values of  15 is as follow
# Binary:       0b1111
# Octal:        0o17
# Hexadecimal:  0xf

# 4. Write a Python Program To Find ASCII value of a character?

char = input ("Enter a character: ")

print ("ANCII value of {} is {}".format(char, ord(char)))

# Enter a character: h
# ANCII value of h is 104

# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print ("For addition        : +")
print ("For subtraction     : -")
print ("For multiplication  : *")
print ("For division        : /")

opr = input("Enter an operator from above list for mathematical operation: 4")

if opr == "+":
    output = num1 + num2
elif opr == "-":
    output = num1 - num2
elif opr == "*":
    output = num1 * num2
elif opr == "/":
    output = num1 / num2

print ("Answer =", output)

# Enter first number: 4
# Enter second number: 4
# For addition        : +
# For subtraction     : -
# For multiplication  : *
# For division        : /
# Enter an operator from above list for mathematical operation: 4*
# Answer = 16