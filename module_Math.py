import math
# finding square root
print(math.sqrt(100))
# without using math module
n=int(input("enter a number"))
print(n**0.5)

# finding power
print(math.pow(5,2))
# without using math module
n=int(input("enter a number"))
print(n**2)

# Finding Area of circle
radius = 5
area = math.pi * math.pow(radius, 2)
print("Area of circle:", area)

#finding factorial
print(math.factorial(5))
# without using math module
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# finding floor
print(math.floor(12.5))
# without using math module
floatnumber=float(input("enter a float number :"))
print(floatnumber//1)

# finding ceil
print(math.ceil(12.6))
# without using math module
ceilnumber=float(input("enter a float number :"))
print((ceilnumber//1)+1)


# Finding the value of pi
print(math.pi)

# Finding Eulers number 
print(math.e)

# Finding Natural logarithm
print(math.log(50))

# Finging sine angle in radians
print(math.sin(90))

# Finding Tan angle in radians
print(math.tan(45))