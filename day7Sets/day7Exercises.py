# Exercises: Day 7
# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set it_companies

print(len(it_companies))

# Add 'Twitter' to it_companies

it_companies.add("Twitter")

# Insert multiple IT companies at once to the set it_companies

it_companies.update(
    {
        "Microsoft",
        "Apple",
        "Google",
        "Amazon",
        "IBM",
        "Oracle",
        "Intel",
        "Cisco",
        "SAP",
        "Accenture",
        "HP",
        "Dell",
        "Salesforce",
        "VMware",
        "NVIDIA",
        "Adobe",
        "Samsung Electronics",
        "Tata Consultancy" "Services",
        "Infosys",
        "Capgemini",
        "Deloitte",
    }
)
print(it_companies)

# Remove one of the companies from the set it_companies

it_companies.remove("Microsoft")
it_companies.remove("Apple")
print(it_companies)

# What is the difference between remove and discard

"""When We use remove() in a data that does not exist in the set, it will rise an error. When We use discard() in a data that does not exist in the set, it will not raise an error"""

# Exercises: Level 2

# Join A and B

A_U_B = A.union(B)
print(A_U_B)

"""A.update(B)
print(A)"""

# Find A intersection B

intersection = A.intersection(B)
print(intersection)

# Is A subset of B

print(A.issubset(B))

# Are A and B disjoint sets

print(A.isdisjoint(B))

# Join A with B and B with A

A_U_B = A.union(B)
B_U_A = B.union(A)
print(A_U_B)
print(B_U_A)

# What is the symmetric difference between A and B

print(A.symmetric_difference(B))

# Delete the sets completely

del it_companies
# print(it_companies)

# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_set = set(age)

len_age_list = len(age)
len_age_set = len(age_set)

if len_age_list > len_age_set:
    print(f"The age list {len_age_list} is bigger than the age set {len_age_set}")
else:
    print(f"The age set {len_age_set} is bigger than the age list {len_age_list}")

# Explain the difference between the following data types: string, list, tuple and set

"""String is a sequence of characters, list is a collection of items in a particular order, tuple is an immutable list and set is an unordered collection of unique items."""

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

text = "I am a teacher and I love to inspire and teach people."

formatted_text = ", ".join(text.split())
print(formatted_text)

text_set = set(formatted_text.split(", "))
print(text_set)
print(len(text_set))

# What is split() used for?

"""The split() method returns a list where the string has been split at each match."""
