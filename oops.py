# Classes and Objects
class student():
  def __init__(self,name ,country):
    self.name=name
    self.country=country
  def start(self):
    return "i am "+self.name + " and iam from " + self.country
# Creating an object
student1=student("subbu","india") 
print(student1)
print(student1.start()) 


class areaofrectangle():
  def __init__(self,len,width):
    self.length=len
    self.width=width
  def area(self):
    return self.length * self.width
# creating an object
area1=areaofrectangle(5,6)
print(area1)
print(area1.area())


# Inheritance
# Inheritance is an OOP concept where a class (called a child or subclass) can access properties and methods of another class (called a parent or superclass).
# Types of Inheritance in Python
# Single Inheritance

class geometry():
  def __init__(self):
    pass
  def area(self,radious):
    self.radious=radious
    return 3.14*self.radious **2
class square(geometry):
  def __init__(self):
    pass
  def area(self,side_value):
    self.side=side_value
    return self.side**2
  def info(self):
    return "this is a square class"
geometry_1=geometry()
square_1=square()

class arthemeticoperations():
  def __init__(self):
    print('this is a parent class')
  def square(self,number):
    self.number=number
    return self.number**2
class cube(arthemeticoperations):
  def __init__(self,value):
    self.value=value
  def cube(self):
    return self.value**3
arthemetic=arthemeticoperations()
cube_1=cube(5)

# Multiple Inheritance

class Test(geometry,arthemeticoperations):
  def __init__(self):
    print("tring to inherit multiple classes at once")
  def info(self):
    print("this is just to test if multiple inheritance works")
  def area(self,number_value):
    self.number=number_value
    return number_value**2
test_1=Test()
test_1.square(5)
test_1.info()

# Multi-level Inheritance

class employee():
  def name(self):
    print("employee Name : subbu")

class salary(employee):
  def sal(self):
    print("salary of an employee : 5lpa")

class designation(salary):
  def desig(self):
    print("the employee is working as a developer")

employee_1=employee()
designation_1=designation()
designation_1.name()

# Hierarchical Inheritance

class Vehicle:
    def show_info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_feature(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def bike_feature(self):
        print("Bike has 2 wheels")

# Creating objects
c = Car()
b = Bike()

c.show_info()      # from Vehicle
c.car_feature()

b.show_info()      # from Vehicle
b.bike_feature()


# Hybrid Inheritance
# When more than one type of inheritance (like single, multiple, hierarchical) is combined, it’s called Hybrid Inheritance.

class Person:
    def person_info(self):
        print("General person info")

class Employee(Person):
    def employee_info(self):
        print("This is an employee")

class Student(Person):
    def student_info(self):
        print("This is a student")

# Hybrid: Multiple Inheritance + Hierarchical
class WorkingStudent(Employee, Student):
    def working_student_info(self):
        print("This is a working student")

ws = WorkingStudent()

ws.person_info()          # From Person (via both paths)
ws.employee_info()        # From Employee
ws.student_info()         # From Student
ws.working_student_info() # From itself