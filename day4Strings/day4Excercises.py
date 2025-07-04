"""Exercises - Day 4"""

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

str1 = "Thirty"
str2 = "Days"
str3 = "Of"
str4 = "Python"
print(f"{str1} {str2} {str3} {str4}")

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
strings = ["Coding", "For", "All"]
text = " ".join(strings)
print(text)

# Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# Print the variable company using print().

print(company)

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize().title().swapcase())

# Cut(slice) out the first word of Coding For All string.

print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

string = "Coding"
print(company.index(string))
print(company.find(string))
print(string in company)

# Replace the word coding in the string 'Coding For All' to Python.

print(company.replace("Coding", "Python"))

# Change Python for Everyone to Python for All using the replace method or other methods.

print(company.replace("All", "Everyone"))

# Split the string 'Coding For All' using space as the separator (split()) .

print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))
# print("\n".join(companies).split())

# What is the character at index 0 in the string Coding For All.

print(company[0])

# What is the last index of the string Coding For All.

print(len(company) - 1)

# What character is at index 10 in "Coding For All" string.

print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.

text = "Python For Everyone"
init = [string[0].upper() for string in text.split()]
print("".join(init))


# Create an acronym or an abbreviation for the name 'Coding For All'.

text = "Coding For All"
init = [string[0].upper() for string in text.split()]
print("".join(init))

# Use index to determine the position of the first occurrence of C in Coding For All.

text = "Coding For All"
print(text.find("C"))

# Use index to determine the position of the first occurrence of F in Coding For All.

text = "Coding For All"
print(text.find("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.

text = "Coding For All People"
print(text.rfind("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

text = "You cannot end a sentence with because because because is a conjunction"
print(text.find("because"))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

text = "You cannot end a sentence with because because because is a conjunction"
print(text.rfind("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

text = "You cannot end a sentence with because because because is a conjunction"
print(text.replace("because because because", ""))

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

text = "You cannot end a sentence with because because because is a conjunction"
print(text.find("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

text = "You cannot end a sentence with because because because is a conjunction"
print(text.replace("because because because", ""))

# Does ''Coding For All' start with a substring Coding?

text = "Coding For All"
print(text.startswith("Coding"))

# Does 'Coding For All' end with a substring coding?

text = "Coding For All"
print(text.endswith("Coding"))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

text = "   Coding For All      "
print(text.strip(" "))

"""Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python"""

text1 = "30DaysOfPython"
text2 = "thirty_days_of_python"
print(text1.isidentifier())
print(text2.isidentifier())


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

python_libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(" #".join(python_libraries))

"""Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next."""

print("I am enjoying this challenge.\nI just wonder what is next.")
print(
    """I am enjoying this challenge.
I just wonder what is next."""
)

"""Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
"""

seq = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(seq.expandtabs(10))

"""Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2

The area of a circle with radius 10 is 314 meters square"""

radius = 10
area = 3.14 * radius**2
print(f"The area of the circle with radius {radius} is {area:.2f} meters square")

""".
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144"""

a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b:.2f}")
print(f"{a} // {b} = {a // b:.2f}")
print(f"{a} ** {b} = {a ** b}")
