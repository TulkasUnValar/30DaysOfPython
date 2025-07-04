"""Introduction

Python is a high-level programming language for general-purpose programming. It is an open source, interpreted, objected-oriented programming language. Python was created by a Dutch programmer, Guido van Rossum. The name of the Python programming language was derived from a British sketch comedy series, Monty Python's Flying Circus. The first version was released on February 20, 1991. This 30 days of Python challenge will help you learn the latest version of Python, Python 3 step by step. The topics are broken down into 30 days, where each day contains several topics with easy-to-understand explanations, real-world examples, and many hands on exercises and projects.

This challenge is designed for beginners and professionals who want to learn python programming language. It may take 30 to 100 days to complete the challenge. People who actively participate in the telegram group have a high probability of completing the challenge.

This challenge is easy to read, written in conversational English, engaging, motivating and at the same time, it is very demanding. You need to allocate much time to finish this challenge. If you are a visual learner, you may get the video lesson on Washera YouTube channel. You may start from Python for Absolute Beginners video. Subscribe the channel, comment and ask questions on YouTube vidoes and be proactive, the author will eventually notice you.

Why Python?

It is a programming language which is very close to human language and because of that, it is easy to learn and use. Python is used by various industries and companies (including Google). It has been used to develop web applications, desktop applications, system administration, and machine learning libraries. Python is a highly embraced language in the data science and machine learning community. I hope this is enough to convince you to start learning Python. Python is eating the world and you are killing it before it eats you.
"""

"""Basic Python

Python Syntax
A Python script can be written in Python interactive shell or in the code editor. A Python file has an extension .py.

Python Indentation
An indentation is a white space in a text. Indentation in many languages is used to increase code readability; however, Python uses indentation to create blocks of code. In other programming languages, curly brackets are used to create code blocks instead of indentation. One of the common bugs when writing Python code is incorrect indentation.

Comments
Comments play a crucial role in enhancing code readability and allowing developers to leave notes within their code. In Python, any text preceded by a hash (#) symbol is considered a comment and is not executed when the code runs.

Example: Single Line Comment

    # This is the first comment
    # This is the second comment
    # Python is eating the world

Example: Multiline Comment

Triple quote can be used for multiline comment if it is not assigned to a variable"""

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""

# This is the first comment
# This is the second comment
# Python is eating the world

# ---------------------------------------------------------------

"""
Data types

In Python there are several types of data types. Let us get started with the most common ones. Different data types will be covered in detail in other sections. For the time being, let us just go through the different data types and get familiar with them. You do not have to have a clear understanding now.

Number
Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Example 1 + j, 2 + 4j

"""
int = -3
float = -2.25
complex = 1 + 2j  # complex number
print(int)  # prints the integer
print(float)  # prints the float
print(complex)  # prints the complex number


"""
String
A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

Example:
'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
"""

name = "Asabeneh"
country = "Finland"
language = "Python"
sentence = "I hope you are enjoying the first day of 30DaysOfPython Challenge"
print(name)  # prints the name
print(country)  # prints the country
print(language)  # prints the language
print(sentence)  # prints the sentence

"""
Booleans
A boolean data type is either a True or False value. T and F should be always uppercase.

Example:
    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False"""

"""
List
Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.
"""

numbers = [1, 2, 3, 4, 5]  # all are the same data types - a list of numbers

fruits = [
    "Banana",
    "Orange",
    "Mango",
    "Avocado",
]  # all the same data types - a list of strings (fruits)

countries = [
    "Finland",
    "Estonia",
    "Sweden",
    "Norway",
]  # all the same data types - a list of strings (countries)

list = [
    "Banana",
    10,
    False,
    9.81,
]  # different data types in the list - string, integer, boolean and float

print(numbers)  # prints the list of numbers
print(fruits)  # prints the list of fruits
print(countries)  # prints the list of countries
print(list)  # prints the list of different data types
print(list[0])  # prints the first element of the list
print(list[1])  # prints the second element of the list
print(list[2])  # prints the third element of the list
print(list[3])  # prints the fourth element of the list

"""
Dictionary
A Python dictionary object is an unordered collection of data in a key value pair format.
"""

mauro = {
    "name": "Mauricio",
    "country": "Quiñones",
    "city": "Cali",
    "age": 39,
    "is_married": False,
    "skills": ["Python", "JavaScript"],
    "address": {
        "street": "Space street",
        "zipcode": "02210",
    },
}

print(mauro)  # prints the dictionary
print(mauro["name"])  # prints the name from the dictionary
print(mauro["country"])  # prints the country from the dictionary
print(mauro["city"])  # prints the city from the dictionary
print(mauro["age"])  # prints the age from the dictionary
print(mauro["is_married"])  # prints the is_married from the dictionary
print(mauro["skills"])  # prints the skills from the dictionary
print(mauro["address"])  # prints the address from the dictionary
print(mauro["address"]["street"])  # prints the street from the dictionary
print(mauro["address"]["zipcode"])  # prints the zipcode from the dictionary

"""
Tuple
A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.
"""

names = ("Asabeneh", "Pawel", "Brook", "Abraham", "Lidiya")
planets = (
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
)
print(names)  # prints the tuple
print(names[0])  # prints the first element of the tuple
print(names[1])  # prints the second element of the tuple
print(planets)
print(planets[0])  # prints the first element of the tuple
print(planets[1])  # prints the second element of the tuple
print(planets[2])  # prints the third element of the tuple
print(planets[3])  # prints the fourth element of the tuple

"""
Set
A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

In later sections, we will go in detail about each and every Python data type.
"""

set_of_numbers = {1, 2, 3, 4, 5}  # a set of numbers
set_of_numbers2 = {3.14, 9.81, 2.7}  # order is not important in set
print(set_of_numbers)  # prints the set of numbers
print(set_of_numbers2)  # prints the set of numbers

"""Checking Data types
To check the data type of certain data/variable we use the type function. In the following terminal you will see different python data types:"""

type_of_int = type(int)
print(type_of_int)  # prints the type of int

type_of1 = type(float)
print(type_of1)  # prints the type of float

type_of2 = type(complex)
print(type_of2)  # prints the type of complex number

type_of3 = type(sentence)
print(type_of3)  # prints the type of sentence

type_of4 = type(fruits)
print(type_of4)  # prints the type of fruits

type_of5 = type(countries)
print(type_of5)  # prints the type of countries

type_of6 = type(list)
print(type_of6)  # prints the type of list

type_of7 = type(mauro)
print(type_of7)  # prints the type of mauro

type_of8 = type(planets)
print(type_of8)  # prints the type of planets

type_of9 = type(set_of_numbers)
print(type_of9)  # prints the type of set_of_numbers
