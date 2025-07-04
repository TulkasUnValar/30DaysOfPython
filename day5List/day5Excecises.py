from countriesData import new_countries

# Exercises: Day 5

# Exercises: Level 1

# Declare an empty list

empty_list = []
empty_list = list()

# Declare a list with more than 5 items

nums = [1, 2, 3, 4, 5]

# Find the length of your list

print(len(nums))

# Get the first item, the middle item and the last item of the list

print(nums[0])
middle_index = len(nums) // 2
print(nums[middle_index])
print(nums[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Tulkas", 10000, 1.80, True, "Valinor"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()

print(it_companies)

# Print the number of companies in the list

print(len(it_companies))

# Print the first, middle and last company

print(it_companies[0])

# Print the list after modifying one of the companies

it_companies[0] = "Intel"
it_companies[-1] = "CISCO Systems"
print(it_companies)

# Add an IT company to it_companies

it_companies.append("Huawei")
print(it_companies)

# Insert an IT company in the middle of the companies list

middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "Lenovo")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[2] = it_companies[2].upper()
print(it_companies)

# Join the it_companies with a string '#;  '

formatted_companies = "#; ".join(it_companies)
print(formatted_companies)

# Check if a certain company exists in the it_companies list.

print("IBM" in it_companies)

# Sort the list using sort() method

sort_it_companies = sorted(it_companies)
print(sort_it_companies)

# Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list

three_first_companies = it_companies[:3]
print(three_first_companies)

# Slice out the last 3 companies from the list

three_last_companies = it_companies[-3:]
print(three_last_companies)

# Slice out the middle IT company or companies from the list

length = len(it_companies)
middle_index = length // 2
if length % 2 == 1:
    middle_company = it_companies[middle_index]
else:
    middle_company = it_companies[middle_index - 1 : middle_index + 1]

print(middle_company)

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list

middle_index = len(it_companies) // 2
it_companies.remove(it_companies[middle_index])
print(it_companies)

# Remove the last IT company from the list

it_companies.remove(it_companies[-1])
print(it_companies)

# Remove all IT companies from the list

it_companies.clear()
print(it_companies)

# Destroy the IT companies list

del it_companies
# print(it_companies)

"""Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
front_end.extend(back_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = front_end.copy()
print(full_stack)

full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

# Exercises: Level 2

"""The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

sorted_ages = sorted(ages)
print(sorted_ages)

max1 = max(sorted_ages)
min1 = min(sorted_ages)
print(f"Max age: {max1}, Min age: {min1}")

# Add the min age and the max age again to the list

ages.append(min1)
ages.append(max1)
print(ages)

# Find the median age (one middle item or two middle items divided by two)

length = len(ages)
middle_index = length // 2
if length % 2 == 1:
    middle_ages = ages[middle_index]
else:
    middle_ages = ages[middle_index - 1 : middle_index + 1]

print(middle_ages)

# Find the average age (sum of all items divided by their number )

sum_ages = sum(ages)
average_ages = sum_ages / len(ages)
print(average_ages)

# Find the range of the ages (max minus min)

max_age = max(ages)
min_age = min(ages)

print(max_age - min_age)

# Compare the value of (min - average) and (max - average), use abs() method

min_average = abs(min_age - average_ages)
max_average = abs(max_age - average_ages)
print(min_average, max_average)

if max_average > min_average:
    print(f"max_average {max_average} is greater than min_average {min_average}")
else:
    print(f"min_average {min_average} is greater than max_average {max_average}")

# Find the middle country(ies) in the countries list

length = len(new_countries)
middle_index = length // 2
if length % 2 == 1:
    middle_new_countries = new_countries[middle_index]
else:
    middle_new_countries = new_countries[middle_index - 1 : middle_index + 1]

print(middle_new_countries)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
length = len(new_countries)
middle_index = length // 2
first_half = new_countries[:middle_index]
second_half = new_countries[(middle_index + 1) :]
print("First half:", first_half)
print("Second half:", second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
ch, ru, usa, *scandic = countries
print(ch, ru, usa, scandic)
