import math
import statistics
import keyword
from countries_data import countries

"""Exercises: Day 11

Exercises: Level 1"""

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.


def sum(num1, num2):
    return num1 + num2


print(sum(3, 5))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.


def area_of_circle(radius):
    pi = 3.141592653589793
    area = pi * radius**2
    return area


print(area_of_circle(7))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*args):
    total = 0
    for num in args:
        if type(num) not in (int, float):
            return "All arguments must be numbers."
        else:
            total += num
    return total


print(add_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "All arguments must be numbers."
        else:
            total += num
    return total


print(add_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


print(convert_celsius_to_fahrenheit(0))  # 32.0
print(convert_celsius_to_fahrenheit(100))  # 212.0


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.


def check_season(month):
    lower_month = month.lower()
    if lower_month == "march" or lower_month == "april" or lower_month == "may":
        return "Sprint"
    elif lower_month == "june" or lower_month == "july" or lower_month == "august":
        return "Summer"
    elif (
        lower_month == "september"
        or lower_month == "october"
        or lower_month == "november"
    ):
        return "Autumn"
    elif (
        lower_month == "december"
        or lower_month == "january"
        or lower_month == "february"
    ):
        return "Winter"
    else:
        return "Invalid month"


print(check_season("March"))  # Sprint
print(check_season("June"))  # Summer
print(check_season("December"))


# Write a function called calculate_slope which return the slope of a linear equation


def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    slope = (y2 - y1) / (x2 - x1)
    return slope


print(calculate_slope(1, 2, 3, 4))  # 1.0
print(calculate_slope(1, 2, 1, 4))  #

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.


def solve_quadratic_eqn(x, a, b, c):
    result = a * (x**2) + b * x + c
    return result


print(solve_quadratic_eqn(2, 1, -3, 2))  # 0
print(solve_quadratic_eqn(2, 7, 2, 2))


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


def print_list(array):
    for i in array:
        print(i)


numbers = [1, 2, 3, 4, 5]
print_list(numbers)
fruits = ["Apple", "Banana", "Cherry"]
print_list(fruits)
cars = ["Toyota", "Honda", "Ford"]
print_list(cars)
names = ["Alice", "Bob", "Charlie"]
print_list(names)


"""Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]"""


def reversed_list(array):
    list = []
    for i in reversed(array):
        list.append(i)
    return list


numbers = [1, 2, 3, 4, 5]
print(reversed_list(numbers))  # [5, 4, 3, 2, 1]

letters = ["A", "B", "C"]
print(reversed_list(letters))  # ["C", "B", "A"]

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(array):
    capitalize_list = []
    for i in array:
        capitalize_list.append(i.capitalize())
    return capitalize_list


fruits = ["apple", "banana", "cherry"]
print(capitalize_list_items(fruits))  # ['Apple', 'Banana', 'Cherry']


"""Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
"""


def add_item(array, *args):
    array.append(*args)
    return array


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_staff, "Meat"))

print(add_item(food_staff, ["Meat", "Fish", "Eggs"]))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

"""Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
"""


def remove_item(array, *args):
    array.remove(*args)
    return array


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(remove_item(food_staff, "Mango"))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))


"""Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
"""


def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.


def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total


print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.


def sum_of_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total


print(sum_of_even(5))  # 6
print(sum_of_even(10))  # 30
print(sum_of_even(100))  # 2550

# Exercises: Level 2

"""Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51."""


def count_evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i & 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}. The number of evens are {evens}."


print(count_evens_and_odds(100))
print(count_evens_and_odds(150))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


print(factorial(5))  # 120


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return math.factorial(n)


print(factorial(5))
print(factorial(7))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not


def is_empty(param):
    if param == [] or param == () or param == {} or param == "":
        return "The parameter is empty."
    return "The parameter is not empty."


print(is_empty([]))
print(is_empty(()))
print(is_empty({}))
print(is_empty(""))
print(is_empty(24))

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).


def statistics_1(array):
    mean = statistics.mean(array)
    median = statistics.median(array)
    mode = statistics.mode(array)
    range = max(array) - min(array)
    variance = statistics.variance(array)
    std = statistics.stdev(array)
    return f"Mean:{mean}, median: {median}, mode: {mode}, range: {range}, variance: {variance:.2f}, std: {std:.2f}"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(statistics_1(numbers))

# Exercises: Level 3

# Write a function called is_prime, which checks if a number is prime.


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


print(is_prime(11))  # True
print(is_prime(15))  # False
print(is_prime(29))  # True
print(is_prime(1))  # True
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # True
print(is_prime(5))  # True
print(is_prime(6))  # True
print(is_prime(0))


# Write a functions which checks if all items are unique in the list.
def unique_items(array):
    return len(array) == len(set(array))


fruits = ["banana", "orange", "mango", "lemon", "orange", "banana"]
print(unique_items(fruits))  # False


fruits = ["banana", "orange", "mango", "lemon"]
print(unique_items(fruits))  # True

# Write a function which checks if all the items of the list are of the same data type.


def same_data_type(array):
    return all(isinstance(item, type(array[0])) for item in array)


fruits = ["banana", "orange", "mango", "lemon"]
print(same_data_type(fruits))  # True

fruits = ["banana", "orange", "mango", 7]
print(same_data_type(fruits))  # False

# Write a function which check if provided variable is a valid python variable

"""
    Check if a string is a valid Python variable name.
    
    Rules:
    1. Cannot be a Python keyword
    2. Cannot start with a number
    3. Can only contain letters, numbers, and underscores
    4. Cannot contain spaces or special characters
    5. Cannot be empty
    """


def valid_variable(name):
    # Check if empty
    if not name:
        return False
    # Check if it´s a Python keyword
    if keyword.iskeyword(name):
        return False
    # Check the first character
    if not (name[0].isalpha() or name[0] == "_"):
        return False
    # Check remaining characters
    for char in name[1:]:
        if not (char.isalnum() or char == "_"):
            return False
    return True


print(valid_variable("my_variable"))  # True
print(valid_variable("2nd_variable"))  # False
print(valid_variable("my-variable"))  # False
print(valid_variable("my variable"))  # False
print(valid_variable(""))  # False
print(valid_variable("_valid_variable"))  # True
print(valid_variable("if"))
print(valid_variable("my&variable"))  # False

# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order


def most_spoken_languages(countries):
    language_count = {}
    for country in countries:
        for language in country["languages"]:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    sorted_languages = []
    for language, count in language_count.items():
        sorted_languages.append((count, language))

    sorted_languages.sort(reverse=True)
    top_10_languages = sorted_languages[:20]
    print(top_10_languages)


most_spoken_languages(countries)

# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.


def most_populated_countries(countries):
    country_populations = []
    for country in countries:
        country_populations.append((country["population"], country["name"]))

    country_populations.sort(reverse=True)
    top_10_countries = country_populations[:20]
    print(top_10_countries)


most_populated_countries(countries)
