# 1. Check if a Number is Even or Odd


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Check if a Year is a Leap Year

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



# 3. Divisible by both 3 and 5

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")



# 4. Eligible to Vote

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



# 5. Check if a number is a multiple of 10

num = int(input("Enter a number: "))
if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")



# 6. Compare two numbers and print the smaller one

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print("Smaller number is:", a)
else:
    print("Smaller number is:", b)




# 7. Classification based on divisibility

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Odd" if num % 2 != 0 else "Not divisible by 2 or 5")



# 8. Age classification

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")



# 9. Check range of a number

num = int(input("Enter a number: "))
if num < 0:
    print("Below 0")
elif num < 10:
    print("Between 0 and 10")
elif num < 50:
    print("Between 10 and 50")
else:
    print("Above 50")




# 10. Temperature to Fahrenheit & Comment

celsius = float(input("Enter temperature in Celsius: "))
if celsius < 0:
    print("Below freezing point")
elif celsius < 25:
    print("Cool")
elif celsius <= 40:
    print("Warm")
else:
    print("Hot")


# 1.Basic Input with Integer Conversion
# Take two numbers as input from the user, convert them to integers, and print their sum
a=int(input("Enter 1st number :"))
b=int(input("Enter a 2nd number :"))
print("a+b =",a+b)

# 2. Multiple Inputs with Space Separation
a, b = map(float, input("Enter two numbers: ").split())
print("Product:", a * b)

# 3. Expression Evaluation with eval()
expr = input("Enter a mathematical expression: ")
print("Result:", eval(expr))

# 4. List Input using eval()
lst = eval(input("Enter a list of numbers: "))
print("Sum:", sum(lst))

# 5. Boolean Type Conversion
val = input("Enter any value: ")
print("Boolean conversion:", bool(val))

# 6. String to Float Conversion
num = input("Enter a number: ")
f = float(num)
print("Square:", f ** 2)

# 7. Dictionary Input using eval()
d = eval(input("Enter a dictionary: "))
print("Keys:", d.keys())
print("Values:", d.values())

# 8. List of Integers from Space Separated Input
nums = list(map(int, input("Enter integers separated by space: ").split()))
print("Maximum:", max(nums))
print("Minimum:", min(nums))


# 9. Mixed Type Literal Input with eval()
data = eval(input("Enter any Python literal: "))  # e.g., "hello", [1,2], (1,2)
print("Type of input:", type(data))

# 10. Combined Type Conversion
a = int(input("Enter an integer: "))
b = float(input("Enter a floating-point number: "))
print("Sum:", a + b)





