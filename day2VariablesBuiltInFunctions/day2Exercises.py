# Day 2: 30 days of Python programming

"""Exercises: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line
"""

first_name = "Tulkas"
last_name = "UnValar"
full_name = f"{[first_name]} {last_name}"
country = "Valinor"
city = "Valmar"
age = 10000
year = 967
is_married = False
is_true = True
is_light_on = True

strength, dexterity, constitution, intelligence, wisdom, charisma = (
    27,
    20,
    24,
    18,
    16,
    14,
)

"""
Exercises: Level 2
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
  """

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(strength))
print(type(dexterity))
print(type(constitution))
print(type(intelligence))
print(type(wisdom))
print(type(charisma))

print(len(first_name))  # Length of first name

if len(first_name) > len(last_name):
    print(f"{first_name} is longer than {last_name}")
else:
    print(f"{last_name} is longer than {first_name}")

num_one = 5
num_two = 4

sum = num_one + num_two
print(sum)

diff = num_one - num_two
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

modulus = num_one % num_two
print(modulus)

exp = num_one**num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

"""Area of circle

A = πr^2
where:
A = Area
r = Radio of circle
π ≈ 3.1416
"""

radio = 30
area_of_circle = 3.1416 * (radio**2)
print(area_of_circle)

"""Circum_of_circle

C=2πr
"""
circum_of_circle = 2 * 3.1416 * radio
print(circum_of_circle)

radio2 = float(input("Enter the radius of the circle: "))
area_of_circle2 = 3.1416 * (radio2**2)
print(f"The area of the circle is: {area_of_circle2}")

first_name_input = input("Enter your first name: ")
last_name_input = input("Enter your last name: ")
country_input = input("Enter your country: ")
age_input = int(input("Enter your age: "))

print(
    f"Hello {first_name_input} {last_name_input}, you are from {country_input}, you are {age_input} years old"
)

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
help(hex)
help(id)
help(int)
help(isinstance)
help(iter)
