# ITERATORS: Objects that let you loop through data one element at a time
numbers = [1, 2, 3, 4]
my_iterator = iter(numbers)  # Convert list to iterator

print(next(my_iterator))  
print(next(my_iterator))  
print(next(my_iterator)) 


#  Generator that yields numbers from 1 to 3
def number_generator():
    yield 1
    yield 2
    yield 3
g=number_generator()
print(next(g))
# for num in number_generator():
#     print(num)

# DECORATORS: Functions that modify the behavior of other functions
def decorator(fun):
    def wrapper():
        print("before function")
        fun()
        print("after function")
    return wrapper
@decorator
def greet():
    print("hello")
print(greet())

