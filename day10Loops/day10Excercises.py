from countries import countries
from countries_data import countries

"""Exercises: Day 10

Exercises: Level 1"""

# Iterate 0 to 10 using for loop, do the same using while loop.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    print(num)

for num in range(11):
    print(num)

count = 0
while count <= 10:
    print(count)
    count += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
for num in range(10, -1, -1):
    print(num)

count = 10
while count >= 0:
    print(count)
    count -= 1

"""Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######"""

count = 0
while count <= 7:
    print("#" * count)
    count += 1

"""Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

count = 0
while count <= 7:
    print("# " * 8)
    count += 1

"""Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""

for num in range(11):
    print(f"{num} x {num} = {num * num}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

skills = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for skill in skills:
    print(skill)

# Use for loop to iterate from 0 to 100 and print only even numbers

for num in range(0, 101, 2):
    print(num)

# Use for loop to iterate from 0 to 100 and print only odd numbers

for num in range(1, 101, 2):
    print(num)

# Exercises: Level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers. The sum of all numbers is 5050..

sum = 0
for num in range(101):
    sum += num
print(sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds. The sum of all evens is 2550. And the sum of all odds is 2500..

sum = 0
for num in range(0, 101, 2):
    sum += num
print(sum)


# Exercises: Level 3

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

for country in countries:
    if "land" in country:
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ["banana", "orange", "mango", "lemon"]
for fruit in reversed(fruits):
    print(fruit)

"""Go to the data folder and use the countries_data.py file.

# What are the total number of languages in the data"""

total_languages = 0
for country in countries:
    total_languages += len(country["languages"])
print(total_languages)

# Find the ten most spoken languages from the data

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
top_10_languages = sorted_languages[:10]
print(top_10_languages)

# Find the 10 most populated countries in the world

country_populations = []
for country in countries:
    country_populations.append((country["population"], country["name"]))

country_populations.sort(reverse=True)
top_10_countries = country_populations[:10]
print(top_10_countries)
