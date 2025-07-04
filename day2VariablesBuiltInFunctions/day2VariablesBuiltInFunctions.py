"""Variables, Builtin Functions"""

"""
In Python we have lots of built-in functions. Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring. Some of the most commonly used Python built-in functions are the following: print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir(). In the following table you will see an exhaustive list of Python built-in functions taken from python documentation: https://docs.python.org/3.9/library/functions.html.

abs()
delattr()
hash()
memoryview()
set()
all()
dict()
help()
min()
setattr()
any()
dir()
hex()
next()
slice()
ascii()
divmod()
id()
object()
sorted()
bin()
enumerate()
input()
oct()
staticmethod()
bool()
eval()
int()
open()
str()
breakpoint()
exec()
isinstance()
ord()
sum()
bytearray()
filter()
issubclass()
pow()
super()
bytes()
float()
iter()
print()
tuple()
callable()
format()
len()
property()
type()
chr()
frozenset()
list()
range()
vars()
classmethod()
getattr()
locals()
repr()
zip()
compile()
globals()
map()
reversed()
__import__()
complex()
hasattr()
max()
round()

"""

help(len)
help(print)
help(type)
help(int)
help(float)
help(str)
help(input)
help(list)
help(dict)
help(min)
help(max)
help(sum)
help(sorted)
help(open)
help(help)
help(dir)
help(abs)
help(all)
help(any)
help(bin)
help(bool)
help(chr)
help(bytes)
help(bytearray)
help(classmethod)
help(complex)
help(dict)
help(float)
help(frozenset)
help(getattr)
help(hash)

"""
As you can see from the terminal above, Python has got reserved words. We do not use reserved words to declare variables or functions. We will cover variables in the next section.

I believe, by now you are familiar with built-in functions. Let us do one more practice of built-in functions and we will move on to the next section.
"""

min1 = min(20, 10, 5, 2, 1)
max1 = max(20, 10, 5, 2, 1)

min2 = min([20, 10, 5, 2, 1])
max2 = max([20, 10, 5, 2, 1])

print(min1, max1)
print(min2, max2)

"""
Variables
Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
Here are some example of valid variable names:

firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
Invalid variables names

first-name
first@name
first$name
num-1
1num

We will use standard Python variable naming style which has been adopted by many Python developers. Python developers use snake case(snake_case) variable naming convention. We use underscore character after each word for a variable containing more than one word(eg. first_name, last_name, engine_rotation_speed). The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

When we assign a certain data type to a variable, it is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable. The equal sign in Python is not equality as in Mathematics.

Example:

# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
Let us use the print() and len() built-in functions. Print function takes unlimited number of arguments. An argument is a value which we can be passed or put inside the function parenthesis, see the example below.

Example:
"""

first_name = "Tulkas"
last_name = "UnValar"
country = "Mordor"
city = "Minas Tirith"
age = 5000
is_married = False
skills = ["Swordsmanship", "Leadership", "Strategy"]
person_info = {
    "first_name": first_name,
    "last_name": last_name,
    "country": country,
    "city": city,
}
print(len(first_name))  # prints the length of the first name
print(len(last_name))  # prints the length of the last name
print(len(country))  # prints the length of the country
print(len(city))  # prints the length of the city
print(len(skills))  # prints the length of the skills list

print(person_info)
print(len(person_info))  # prints the number of key-value pairs in the dictionary

person_info2 = {
    "firstname": "Mauro",
    "lastname": "Quiñones",
    "country": "Colombia",
    "city": "Cali",
}

print(person_info2)
print(
    len(person_info2)
)  # prints the number of key-value pairs in the second dictionary

print("Hello madafokas")

print(
    f"Hello {first_name} {last_name}, you are from {country}, you live in {city}, you are {age} years old, married: {is_married}, your skills are: {', '.join(skills)}."
)

print(
    f"Hello {person_info['first_name']} {person_info['last_name']}, you are from {person_info['country']}, you live in {person_info['city']}."
)

print(
    "Hello", ",", "World", "!"
)  # it can take multiple arguments, four arguments have been passed
print(len("Hello, World!"))  # prints the length of the string 'Hello, World!'
print(len([1, 2, 3, 4, 5]))  # prints the length of the list [1, 2, 3, 4, 5]
print(
    len({"name": "Tulkas", "country": "Mordorian"})
)  # prints the length of the dictionary
print(len((1, 2, 3)))  # prints the length of the tuple (1, 2, 3)
print(len({1, 2, 3}))  # prints the length of the set {1, 2, 3}
# print(len(True))  # Has no len. prints the length of the boolean value True, which is 1
# print(len(3.14))  # Has no len. prints the length of the float value 3.14, which is 4
# print(len(None))  # Has no len. prints the length of None, which is 0
# print(len(3 + 4.0))  # Has no len. prints the length of the float value 7.0, which is 3
print(
    len({"strength", "intelligence", "wisdom"})
)  # prints the length of the set {'strength', 'intelligence', 'wisdom'}
print(
    len(("Mauricio", "Tulkas"))
)  # prints the length of the tuple ('Mauricio', 'Tulkas'), which is 2

print(
    len(
        f"Hello {person_info['first_name']} {person_info['last_name']}, you are from {person_info['country']}, you live in {person_info['city']}."
    )
)

"""Let us print and also find the length of the variables declared at the top:"""

# Printing the values stored in the variables

print("First name:", first_name)
print("First name length:", len(first_name))
print("Last name: ", last_name)
print("Last name length: ", len(last_name))
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Married: ", is_married)
print("Skills: ", skills)
print("Person information: ", person_info)

"""
Declaring Multiple Variable in a Line

Multiple variables can also be declared in one line:

Example:"""

first_name1, last_name1, country1, city1 = "Tulkas", "UnValar", "Mordor", "Minas Tirith"
print(
    f"Hey, I´m {first_name1} {last_name1}, I am from {country1} and I live in {city1}."
)

"""Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables. Example:"""

"""first_name2 = input("Enter your fucking name: ")
age2 = input("Enter your fucking age: ")

print(first_name2, age2)
"""

"""
Data Types

There are several data types in Python. To identify the data type we use the type built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.
"""

"""
Checking Data types and Casting
Check Data types: To check the data type of certain data/variable we use the type Examples:

"""

first_name = "Asabeneh"  # str
last_name = "Yetayeh"  # str
country = "Finland"  # str
city = "Helsinki"  # str
age = 250  # int

print(type(first_name))  # <class 'str'>
print(type(last_name))  #
print(type(country))  #
print(type(city))  #
print(type(age))  # <class 'int'>
print(type(10))
print(type(3.14))
print(type(4 - 4j))  # complex number
print(type(True))
print(type([1, 2, 3, 4, 5]))  # list
print(type({"name": "Tulkas"}))
print(type(("Tulkas", "UnValar")))  # tuple
print(type(zip([1, 2], [3, 6])))  # zip object

"""
Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.
"""
# int to float
num_int = 10
print("num_int", num_int, type(num_int))
num_float = float(num_int)
print("num_float", num_float, type(num_float))

# float to int
gravity = 9.81
gravity_int = int(gravity)
print("gravity_int", gravity_int, type(gravity_int))

# int to str
num_int = 10
print("num_int", num_int, type(num_int))
num_float = str(num_int)
print("num_float", num_float, type(num_float))

# str to int or float
num_str = "10.6"
print("num_str", num_str, type(num_str))
num_float = float(num_str)
print("num_float", num_float, type(num_float))
num_int = int(num_float)
print("num_int", num_int, type(num_int))

num_int = int(float(num_str))  # Convert string to float and then to int
print("num_int", num_int, type(num_int))

full_name = "Tulkas UnValar"
print("full_name", full_name, type(full_name))
full_name_to_list = list(full_name)
print("full_name_to_list", full_name_to_list, type(full_name_to_list))
full_name_to_tuple = tuple(full_name)
print("full_name_to_tuple", full_name_to_tuple, type(full_name_to_tuple))
full_name_to_set = set(full_name)
print("full_name_to_set", full_name_to_set, type(full_name_to_set))

"""
Numbers
Number data types in Python:

Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...

Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j
"""
