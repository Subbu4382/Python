# Errors And Exceptions

#  Print the sum of digits of a number entered by the user
try:
   def sum_digit():
    n=int(input("Enter a number :"))
    sum = 0
    while n:
        digit = n%10
        sum =sum+digit
        n=n//10
    return sum
   print(sum_digit())
except Exception as e:
    print(e)

# Catching multiple exceptions
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print(" Cannot divide by zero!")
except ValueError:
    print(" Please enter valid integers.")
finally:
    print("Done executing!")

# Handling errors in Files

try:
    f=open("sample.txt","r")
    a=f.read()
    print(a)
except FileNotFoundError:
    print("file not found")
else:
    print("no error in code")
finally:
    print("program executed")


# Handling List Index Error
items = ["Apple", "Banana", "Cherry"]
try:
    idx = int(input("Enter index (0-2): "))
    print("You selected:", items[idx])
except IndexError:
    print("Index out of range!")
except ValueError:
    print("Please enter a valid number.")
    
# Costum errors 

name=input("enter a name")
print(name)
if len(name)==5:
    raise ValueError("name should be greater tham 5")