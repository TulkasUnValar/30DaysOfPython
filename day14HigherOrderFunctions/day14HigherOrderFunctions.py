"""Higher Order Functions

In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

A function can take one or more functions as parameters
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable
In this section, we will cover:

Handling functions as parameters
Returning functions as return value from another functions
Using Python closures and decorators"""

"""Function as a Parameter"""


def sum_numbers(nums):  # normal function
    return sum(nums)  # a sad function abusing the built-in sum function :<


def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # 15

"""Function as a Return Value"""


def square(x):
    return x**2


def cube(x):
    return x**3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute
    else:
        raise ValueError("Unknown function type")


result = higher_order_function("square")
print(result(3))  # 9
result = higher_order_function("cube")
print(result(3))  # 27
result = higher_order_function("absolute")
print(result(-3))  # 3

"""You can see from the above example that the higher order function is returning different functions depending on the passed parameter"""

"""Python Closures

Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.

Example:"""


def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


print(add_ten()(5))  # 15
print(add_ten()(10))  # 20
print(add_ten()(20))  # 30

# Using the closure function
closure_function = add_ten()
print(closure_function(5))  # 15
print(closure_function(10))  # 20
print(closure_function(20))  # 30

"""Python Decorators

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate."""

"""Creating Decorators

To create a decorator function, we need an outer function with an inner wrapper function."""


def greetings():
    return "Welcome madafocas"


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


g = uppercase_decorator(greetings)
print(g())


## Let us implement the example above with a decorator

"""This decorator function is a higher order function
that takes a function as a parameter"""


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def greetings():
    return "Hello bitches"


print(greetings())  # HELLO BITCHES

"""Applying Multiple Decorators to a Single Function"""

"""These decorator functions are higher order functions
that take functions as parameters"""


# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        split_string = func.split()
        return split_string

    return wrapper


@split_string_decorator
@uppercase_decorator  # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return "Hello bitches, how are you doing today?"


print(greeting())

"""Accepting Parameters in Decorator Functions

Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters."""


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(par1, par2, par3):
        function(par1, par2, par3)
        print("I live in {}".format(par3))

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, city):
    print("My name is {} {}. I love fighting".format(first_name, last_name, city))


print_full_name("Tulkas", "UnValar", "Mordor")


def decorator_with_parameters(function):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = function(*args, **kwargs)
        print("After the function call")
        return result

    return wrapper


@decorator_with_parameters
def hello(name="John Doe"):
    print(f"Hello {name}")


hello("Alice")  # Before the function call

"""Built-in Higher Order Functions

Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce. Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce."""


"""Python - Map Function

The map() function is a built-in function that takes a function and iterable as parameters.

    # syntax
    map(function, iterable)"""

# Example 1
numbers = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x**2  # function to be applied to each element of the iterable


numbers_squared = map(square, numbers)
print(list(numbers_squared))

numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))

# Example 2
numbers_str = ["1", "2", "3", "4", "5"]  # iterable of strings
numbers_int = list(
    map(int, numbers_str)
)  # convert strings to integers using map function
print(numbers_int)  # [1, 2, 3, 4, 5]

# Example 3

names = ["Alice", "Bob", "Charlie"]  # iterable of strings


def upper_case(name):
    return name.upper()


names_upper_cased = list(map(upper_case, names))
print(names_upper_cased)


# Let us apply it with a lambda function
names_upper_cased = list(map(lambda name: name.upper(), names))
print(names_upper_cased)  # ['ALICE', 'BOB', 'CHARLIE']
# What actually map does is iterating over a list. For instance, it changes the names to upper case and returns a new list.

"""Python - Filter Function

The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.

    # syntax
    filter(function, iterable)"""

# Example 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # iterable


def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]


# Example 2
def is_odd(num):
    if num % 2 != 0:
        return True
    return False


odd_numbers = list(filter(is_odd, numbers))
print(odd_numbers)


# Example 3
# Filter long name
names = ["Alice", "Bob", "Charlie", "David", "Eve"]  # iterable


def is_name_long(name):
    if len(name) > 4:
        return True
    return False


long_names = list(filter(is_name_long, names))
print(long_names)

long_names = list(filter(lambda name: len(name) > 6, names))
print(long_names)


"""Python - Reduce Function

The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value. 

Example:1"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # iterable


def add_two_numbers(x, y):
    return int(x) + int(y)


sum_of_numbers = reduce(add_two_numbers, numbers)
print(sum_of_numbers)
