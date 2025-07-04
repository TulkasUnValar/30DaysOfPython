"""Functions
So far we have seen many built-in Python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, let us learn what a function is and why we need them?

Defining a Function
A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the def keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.
"""

"""Declaring and Calling a Function

When we make a function, we call it declaring a function. When we start using the it, we call it calling or invoking a function. Function can be declared with or without parameters.

# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()"""

"""Function without Parameters
Function can be declared without parameters.

Example:"""


def full_name():
    first_name = "Tulkas"
    last_name = "UnValar"
    full_name = f"{first_name} {last_name}"
    print(full_name)


full_name()


def add(x, y):
    return x + y


new_sum = add(2, 5)
print(new_sum)


def subtract():
    num_1 = 10
    num_2 = 5
    subs = num_1 - num_2
    print(subs)


subtract()


def sub(x, y):
    print(x - y)


sub(9, 5)

"""Function Returning a Value - Part 1

Function can also return values, if a function does not have a return statement, the value of the function is None. Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it."""


def full_name():
    first_name = "Tulkas"
    last_name = "UnValar"
    full_name = f"{first_name} {last_name}"
    return full_name


print(full_name())


def add():
    num_1 = 10
    num_2 = 5
    subs = num_1 - num_2
    return subs


print(add())

""""Function with Parameters

In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter

Single Parameter: If our function takes a parameter we should call our function with an argument
  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))"""


def greeting(name):
    message = f"{name}, welcome to the pantheon"
    return message


print(greeting("Tulkas"))


def square_number(num):
    return num * num


print(square_number(5))


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


def print_numbers(array):
    for number in numbers:
        print(number)


print_numbers(numbers)


def area_of_circle(radius):
    pi = 3.14
    area = pi * radius**2
    return area


print(area_of_circle(5))


def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


print(sum_of_numbers(10))
print(sum_of_numbers(100))  # Example usage, should return 5050

"""Two Parameter: A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments. Let us check a function with two parameters:
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))"""


def full_name(first_name, last_name):
    return f"Full name: {first_name} {last_name}"


print(full_name("Tulkas", "UnValar"))


def sum_two_numbers(num1, num2):
    return num1 + num2


print("Sum of two numbers: ", sum_two_numbers(5, 10))


def calculate_age(current_year, birth_year):
    return current_year - birth_year


print("Age: ", calculate_age(2025, 1986))


def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + " N"
    return weight


print("Weight of the object: ", weight_of_object(100, 9.81))


"""Passing Arguments with Key and Value

If we pass the arguments with key and value, the order of the arguments does not matter.

# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here"""


def full_name(first_name, last_name):
    return f"Full name: {first_name} {last_name}"


print(full_name(first_name="Tulkas", last_name="UnValar"))


def add_two_numbers(num1, num2):
    return num1 + num2


print("Sum of two numbers: ", add_two_numbers(num1=34.4, num2=10))


def calculate_age(current_year, birth_year):
    return current_year - birth_year


print("Age: ", calculate_age(current_year=2025, birth_year=1789))


def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + " N"
    return weight


print("Weight of the object: ", weight_of_object(mass=40, gravity=9.81))


"""Function Returning a Value - Part 2

If we do not return a value with a function, then our function is returning None by default. To return a value with a function we use the keyword return followed by the variable we are returning. We can return any kind of data types from a function.

Returning a string: Example:"""


def print_name(firstname):
    return firstname


print_name("Asabeneh")  # Asabeneh


def print_full_name(firstname, lastname):
    space = " "
    full_name = firstname + space + lastname
    return full_name


print_full_name(firstname="Asabeneh", lastname="Yetayeh")

"""Returning a number:"""


def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(2, 3))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print("Age: ", calculate_age(2019, 1819))


"""Returning a boolean:"""


def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_even(10))  # True
print(is_even(11))  # False

"""Returning a list: """


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(10))  # [0, 2, 4, 6, 8, 10]
print(find_even_numbers(21))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def find_odd_numbers(n):
    odds = []
    for i in range(n + 1):
        if i % 2 != 0:
            odds.append(i)
    return odds


print(find_odd_numbers(10))  # [1, 3, 5, 7, 9]
print(find_odd_numbers(21))  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

"""Function with Default Parameters
Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.

# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)"""


def greeting(name="Guest"):
    message = f"{name}, welcome to the pantheon"
    return message


print(greeting())
print(greeting("Tulkas"))


def square_number(num=4):
    return num * num


print(square_number())
print(square_number(5))


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


def print_numbers(array=numbers):
    for number in numbers:
        print(number)


print_numbers()
print_numbers(numbers)


def area_of_circle(radius=7):
    pi = 3.14
    area = pi * radius**2
    return area


print(area_of_circle())
print(area_of_circle(5))


def sum_of_numbers(n=3):
    total = 0
    for i in range(n + 1):
        total += i
    return total


print(sum_of_numbers())
print(sum_of_numbers(10))
print(sum_of_numbers(100))


def generate_full_name(first_name="Tulkas", last_name="UnValar"):
    return f"{first_name} {last_name}"


print(generate_full_name())
print(generate_full_name("Sancho", "Panza"))


"""Arbitrary Number of Arguments

If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)"""


def sum_all_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total


print(sum_all_numbers(1, 2, 3, 4, 5))  # Output: 15
print(sum_all_numbers(10, 20, 30))  # Output: 60

"""Default and Arbitrary Number of Parameters in Functions"""


def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


generate_groups("Team A", "John", "Mike", "Sarah", "Sam")

"""Function as a Parameter of Another Function
"""


# You can pass functions around as parameters
def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 5))  # Output: 25
