# 1 Write a program to print the sum of all even numbers between 1 and 100
def sum_even():
    sum=0
    for i in range(1,101):
        if i%2==0:
            sum +=i
    return sum
a=sum_even()
print(a)
print()
# 2 Write a program that prints the first 10 powers of 2 using a loop
def powers(n):
    for i in range(n+1):
        print(2**i)
print(powers(10))

print()

# 3 Calculate the factorial of a number entered by the user

def factorial():
    n=int(input("Enter a number"))
    sum=1
    for i in range(1,n+1):
        
        sum=sum*i
    return sum
print(factorial())

print()

# 4 Print the reverse of a given number
def reverse():
    num=int(input("Enter a nummber"))
    result=0
    while num:
        digit=num%10
        result=result*10+digit
        num=num//10
    return result
print(reverse())

print()

# 5 Count the number of digits in a given integer using loop
def count_digits():
    num=int(input("Enter a number:"))
    count=0
    while num:
        digit=num%10
        count=count+1
        num=num//10
    return count
print(count_digits())

print()

# 6 Write a program that prints all numbers from 1 to 100 that are divisible by both 3 and 5
def divisible():
    for i in range(1,101):
        if (i %3==0 and i % 5==0):
            print(i)
divisible()

print()

# 7 Without using multiplication calculate a*b using addition and a loop
def multiplication():
    a=10
    b=12
    mul=0
    for i in range(1,b+1):
        mul=mul+a
    return mul
print(multiplication())

print()

# 8 Print the sum of digits of a number entered by the user
def sum_digit():
    n=int(input("Enter a number :"))
    sum = 0
    while n:
        digit = n%10
        sum =sum+digit
        n=n//10
    return sum
print(sum_digit())

print()

# 9 Write a loop to check if a number is a palindrome or not
def palindrome():
    n=int(input("Enter a number :"))
    original=n
    res = 0
    
    while n:
        digit = n%10
        res =res*10+digit
        n=n//10
    print(res)
    if original == res:
        return "Palimdrome"
    else:
        return"not a palindrome"
print(palindrome())
print()


# 10 Write a program to find the highest digit in a given number
def highest():
    n=int(input("Enter a number :"))
    hg=0
    while n:
        digit=n%10
        if digit>hg:
            hg=digit
        n=n//10
    return hg
print(highest())
print()

# 11 Write a program to check if a number is positive , negative or zero
def hello():
    n=int(input("Enter a number :"))
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "zero"
print(hello())
print()

# 12 write a program that takes a number and prints whether it is divisible by 2,3,,both or neither
def divisible():
    n=int(input("Enter a number :"))
    if n%2==0 and n%3==0:
        return"divisible by both 2 and 3"
    elif n%2==0:
        return"divisible by 2"
    elif n%3==0:
        return"divisible by 3"
    else:
        return"not divisible by both 2 and 3"
print(divisible())
print()

# 13 Check if a number is a three-digit number using conditionals
def three_digit():
    n=int(input("enter a number :"))
    count=0
    while n:
        digit = n%10
        count=count +1
        n=n//10
    
    if count==3:
        return "three-digit number"
    else:
        return "not a three-digit number"
print(three_digit())
print()

# 14 Write a program to check whether a given number is prime number
def prime():
    n=int(input("enter a number :"))
    prime=0
    for i in range(2,n):
        if i%2==0:
            prime =0
        else:
            prime =1
    if prime ==0:
        return "prime"
    else:
        return "Not a prime"
print(prime())
print()

# 15. Write a program to find the largest of three numbers entered by the user using nested if-else
def largest_three_num():
    a=int(input("enter 1st number :")) 
    b=int(input("enter 2st number :"))
    c=int(input("enter 3st number :"))
    if a>b:
        if a>c:
            return "a is greater"
        else:
            return "c is greater"
    else:
        if b>c:
            return "b is greater"
        else:
            return "c is greater"
print(largest_three_num())
print()

# 16. Check if a year is a leap year or not.
def leap_year():
    year=int(input("enter a year :"))
    if year %400==0 or(year%4==0 and year %100!=0):
        return "Leap year"
    else:
        return "not a leap year"
print(leap_year())
print()

# 17. Take an integer input and determine if it is even and greater than 50.
def hello():
    n=int(input("enter a number :"))
    if n%2==0:
        if n>50:
            return "even and greater than 50"
        else:
            return "even and less than 50"
    else:
        return "odd"
print(hello())
print()

# 18. Write a program to classify a number as:
# * Less than 0: "Negative"
# * 0 to 9: "Single Digit"
# * 10 to 99: "Two Digits"
# * 100 and above: "Three or More Digits"
def hello():
    num=int(input("enter a number :"))
    if num <0:
        return "negative"
    elif 0<=num<=9:
        return "single digit"
    elif 10<= num <=99:
        return "Two digits"
    elif num>=100:
        return "three or more digits"
    else:
        return "invalid number"
print(hello())
print()


# 19. Write a program to check if the square of a number is greater than 1000, and if yes, print the square.

def square():
    n=int(input("enter a number :"))
    s=n**2
    if s >1000:
        return n,"square is ",s,"is greater than 1000"
    else:
        return n,"square is not greater than 1000"
print(square())
print()

# 20. Take two integers as input and determine if one is a factor of the other.
def hello():
    a=int(input("enter 1st number :"))
    b=int(input("enter 2nd number :"))
    if a % b==0:
        return f"{a} is a factor of {b}"
    elif b % a ==0:
        return f"{b} is a factor of {a}"
    else:
        return f"{a} and {b} are not factors"
print(hello())
print()


# 21 *Armstrong Number Check*
   # Without using string or list, check if a number is an Armstrong number
def Armstrong():
    num=int(input("enter a number :"))
    original =num
    sum = 0
    n=len(str(num))
    while num:
        digit = num%10
        sum = sum+ digit ** n
        num = num//10
   
    if original ==sum:
        return f"{original} is a Armstrong number"
    else:
        return f"{original} not a Armstrong number"  
print(Armstrong())      
print()


# 22. *Prime Digit Count*
#    Count how many digits in a number are prime (2, 3, 5, 7). Do this without converting to string or using arrays.
def prime_digit_count():
    num = int(input("Enter a number: "))
    count = 0
    n = num 

    while n > 0:
        digit = n % 10
        if digit in (2, 3, 5, 7):
            count += 1
        n = n // 10

    return f"Number of prime digits: {count}"

print(prime_digit_count())


