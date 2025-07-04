"""List Comprehension

List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.

# syntax
[i for i in iterable if expression]"""

"""Example:1

For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:"""

# One way
language = "Python"
lst = list(language)  # changing the string to list
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o

"""Example:2

For instance if you want to generate a list of numbers"""

# Generating numbers
numbers = [i for i in range(11)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(
    numbers
)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

"""Example:3

List comprehension can be combined with if expression"""

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

negative_odd_numbers = [i for i in numbers if i % 2 != 0 and i < 0]
print(negative_odd_numbers)  # [-7, -3, -1]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""Lambda Function

Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another function."""


"""Creating a Lambda Function

To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression. See the syntax and the example below. Lambda function does not use return but it explicitly returns the expression.

# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))"""


# Named function
def add_two_nums(a, b):
    return a + b


print(add_two_nums(2, 3))  # 5

# Lets change the above function to a lambda function

add_two_numbers = lambda a, b: a + b
print(add_two_numbers(2, 3))  # 5

# Self invoking lambda function

(lambda a, b: a * b)(
    2, 4
)  # need to encapsulate it in print() to see the result in the console
print((lambda a, b: a * b)(2, 4))  # 8

square = lambda x: x**2
print(square(2))

cube = lambda x: x**3
print(cube(3))

lineal_equation = lambda a, b, c: a**2 + b + 4 * c
print(lineal_equation(2, 3, 4))  # 27

"""Lambda Function Inside Another Function

Using a lambda function inside another function."""


def power(x):
    return lambda n: x**n


def power(x):
    return lambda n: x**n


cube = power(3)(2)
print(cube)

two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32
