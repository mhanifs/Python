# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

num= int(input("Enter a number:"))

if num > 0:
    print("Number {} is positive".format(num))
elif num < 0:
    print("Number {} is negative".format(num))
else:
    print("Number {} is zero".format(num))
# Number 7 is positive

# 2. Write a Python Program to Check if a Number is Odd or Even?

num= int(input("Enter a number:"))
# entered number 7 as input var, any other num can be input fed
if num % 2 == 0:
    print("Number {} is an even number".format(num))
else:
    print("Number {} is an odd number".format(num))

# Number 7 is an odd number


# 3. Write a Python Program to Check Leap Year?

year = int(input("Enter the year:"))
if year % 4 == 0:
    print(year, "is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Enter the year:2005
# 2005 is not a leap year
# Enter the year:2008
# 2008 is a leap year




# 4. Write a Python Program to Check Prime Number?

num = int(input("Enter a number: "))
if num >1:
    for i in range(2, num):
        if (num%i) == 0:
            print(num, " is not a prime number")
            break
    else:
        print(num, " is a prime number")
else:
    print(num, " is not a prime number")

# Enter a number: 13
# 13  is a prime number
#
# Enter a number: 9
# 9  is not a prime number


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

a = 1
b = 100000

print("Prime numbers between", a,  "and", b, "are :")

for num in range(a, b):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

