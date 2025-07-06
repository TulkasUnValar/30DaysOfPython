from functools import reduce
from countries import new_countries
from collections import Counter
from countries_data import countries_info
from itertools import chain

# Exercises: Day 14

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

# Explain the difference between map, filter, and reduce.
"""We use map to iterate over a list and apply a function to each element in the list and return a new list with the results. we use filter to iterate over a list and apply a function to each element in the list and return a boolean value. We use reduce to iterate over a list and apply a function to each element in the list and return a single value"""

# Explain the difference between higher order function, closure and decorator

"""Higher order function is a function that takes a function as a parameter or returns a function.  Closure is a enclosing function that has a nested function which allow as to access to outer scope. Decorator is a function that wraps another function and extends the behavior of the wrapped function without explicitly modifying it."""


# Define a call function before map, filter or reduce, see examples.
def reverse_countries(country):
    return country[::-1]


reversed_countries = list(map(reverse_countries, countries))
print(reversed_countries)

# Use for loop to print each country in the countries list.

for country in countries:
    print(country)

# Use for to print each name in the names list.

for name in names:
    print(name)

# Use for to print each number in the numbers list.
for number in numbers:
    print(number)


# Exercises: Level 2

# Use map to create a new list by changing each country to uppercase in the countries list


def uppercase(country):
    return country.upper()


uppercase_countries = list(map(uppercase, countries))
print(uppercase_countries)


# Use map to create a new list by changing each number to its square in the numbers list


def square(number):
    return number**2


squared_numbers = list(map(square, numbers))
print(squared_numbers)

# Use map to change each name to uppercase in the names list


def uppercase(name):
    return name.upper()


uppercase_names = list(map(uppercase, names))
print(uppercase_names)

# Use filter to filter out countries containing 'land'.


def country_contains_land(country):
    return "land" in country


countries_containing_land = list(filter(country_contains_land, countries))
print(countries_containing_land)


# Use filter to filter out countries having exactly six characters.
def six_characters(country):
    return len(country) == 6


six_characters_countries = list(filter(six_characters, countries))
print(six_characters_countries)

# Use filter to filter out countries containing six letters and more in the country list.


def six_more_characters(country):
    return len(country) >= 6


six_more_characters_countries = list(filter(six_more_characters, countries))
print(six_more_characters_countries)


# Use filter to filter out countries starting with an 'E'
def staring_e(country):
    return country[0] == "E"


countries_staring_e = list(filter(staring_e, countries))
print(countries_staring_e)

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

numbers_str = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


def int_number(number):
    return int(number)


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def add_two_numbers(x, y):
    return int(x) + int(y)


sum_int_odd_numbers = reduce(
    add_two_numbers, filter(is_even, map(int_number, numbers_str))
)


print(sum_int_odd_numbers)


# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.


def get_string_list(number):
    return str(number)


string_list = list(map(get_string_list, numbers))
print(string_list)


# Use reduce to sum all the numbers in the numbers list.


def sum_all_numbers(x, y):
    return int(x) + int(y)


sum_numbers = reduce(sum_all_numbers, numbers)
print(sum_numbers)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

sentence = (
    reduce(
        lambda x, y: f"{x}, {y}" if y != countries[-1] else f"{x}, and {y}", countries
    )
    + " are north European countries"
)

print(sentence)


# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).


def categorize_countries(new_countries):
    patterns = ["land", "ia", "island", "stan"]

    # Verify if a country has a common pattern
    def has_common_patterns(country):
        return any(pattern in country.lower() for pattern in patterns)

    return list(filter(has_common_patterns, new_countries))


print(categorize_countries(new_countries))


# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.


# Using Lambda
def staring_letter_countries(new_countries):
    first_letters = map(lambda country: country[0], new_countries)

    return dict(Counter(first_letters))


print(staring_letter_countries(new_countries))


# No lambda
def get_first_letter(country):
    return country[0]


def staring_letter_countries(new_countries):
    first_letters = map(get_first_letter, new_countries)
    return dict(Counter(first_letters))


print(staring_letter_countries(new_countries))


# No apply to the exercises
def starting_letter_countries(new_countries):
    starting_letters = {}
    for country in new_countries:
        first_letter = country[0]
        if first_letter in starting_letters:
            starting_letters[first_letter] += 1
        else:
            starting_letters[first_letter] = 1

    return starting_letters


print(starting_letter_countries(new_countries))

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.


def get_first_ten(new_countries):
    return list(new_countries[:10])


print(get_first_ten(new_countries))

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.


def get_last_ten(new_countries):
    return list(new_countries[-10:])


print(get_last_ten(new_countries))


# Exercises: Level 3

# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:


# Sort countries by name, by capital, by population

"""def most_populated_countries(countries):
    country_populations = []
    for country in countries:
        country_populations.append((country["population"], country["name"]))

    country_populations.sort(reverse=True)
    top_10_countries = country_populations[:20]
    print(top_10_countries)


most_populated_countries(countries)"""


def sort_by_name(countries_info):
    return sorted(countries_info, key=lambda x: x["name"])


print(sort_by_name(countries_info))


def sort_by_capital(countries_info):
    return sorted(countries_info, key=lambda x: x["capital"])


print(sort_by_capital(countries_info))


def sort_by_population(countries_info):
    return sorted(countries_info, key=lambda x: x["population"])


print(sort_by_population(countries_info))

# Sort out the ten most spoken languages by location.


# Extract the languages of all countries in the world.
def get_languages(countries_info):
    # map to get the languages of each country
    languages_list = map(lambda country: country["languages"], countries_info)
    # chain to flatten the list of lists
    all_languages = list(chain.from_iterable(languages_list))
    return all_languages


# Get the most spoken languages
def most_spoken_languages(countries_info):
    languages = get_languages(countries_info)
    # Count frequency with Counter
    language_counter = Counter(languages)
    # Convert to list of tuples (count, lang) and sort by count
    sorted_languages = sorted(
        [(count, lang) for lang, count in language_counter.items()], reverse=True
    )

    top_10 = sorted_languages[:10]
    return top_10


print(most_spoken_languages(countries_info))

# Sort out the ten most populated countries."


def most_populated(countries_info):
    # Extract name and population for each country using map
    population_data = map(
        lambda country: (country["name"], country["population"]), countries_info
    )
    # Sort by population in descending order
    sorted_population = sorted(population_data, key=lambda x: x[1], reverse=True)

    top_10 = sorted_population[:10]
    return top_10


print(most_populated(countries_info))
