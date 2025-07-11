"""Day 10

Loops

Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

while loop
for loop"""

"""While Loop

We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.

  # syntax
while condition:
    code goes here
"""

count = 0
while count < 5:
    print(count)
    count += 1

"""In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.

  # syntax
while condition:
    code goes here
else:
    code goes here"""

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)

"""The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed."""

"""Break and Continue - Part 1

Break: We use break when we like to get out of or stop the loop.
# syntax
while condition:
    code goes here
    if another_condition:
        break"""

count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break

"""The above while loop only prints 0, 1, 2, but when it reaches 3 it stops."""

"""Continue: With the continue statement we can skip the current iteration, and continue with the next:

  # syntax
while condition:
    code goes here
    if another_condition:
        continue"""

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

"""The above while loop only prints 0, 1, 2 and 4 (skips 3)."""

"""For Loop

A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

For loop with list
# syntax
for iterator in lst:
    code goes here"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number)

"""For loop with string

# syntax
for iterator in string:
    code goes here"""

language = "Tulkas UnVAlar"
for char in language:
    print(char)

for i in range(len(language)):
    print(language[i])

"""For loop with tuple

# syntax
for iterator in tpl:
    code goes here"""

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
for number in numbers:
    print(number)

"""For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
  
  # syntax
for iterator in dct:
    code goes here"""

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)  # this way we get both keys and values printed out

"""Loops in set

# syntax
for iterator in st:
    code goes here"""

it_companies = {
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

for company in it_companies:
    print(company)


"""Break and Continue - Part 2

Short reminder: Break: We use break when we like to stop our loop before it is completed.

# syntax
for iterator in sequence:
    code goes here
    if condition:
        break"""

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
for number in numbers:
    print(number)
    if number == 7:
        break

"""In the above example, the loop stops when it reaches 7."""

"""Continue: We use continue when we like to skip some of the steps in the iteration of the loop.

  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue"""

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
for number in numbers:
    print(number)
    if number == 3:
        continue
    (
        print("Next number should be ", number + 1)
        if number != 20
        else print("loop's end")
    )  # for short hand conditions need both if and else statements
print("outside the loop")

"""In the example above, if the number equals 3, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left."""

"""The Range Function

The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range"""

num_lis = list(range(11))
print(num_lis)

num_st = set(
    range(1, 11)
)  # 2 arguments indicate start and end of the sequence, step set to default 1
print(num_st)

num_list = list(range(0, 11, 2))
print(num_list)

num_set = set(range(0, 11, 2))
print(num_set)


"""# syntax
for iterator in range(start, end, step):"""

for number in range(11):
    print(number)  # prints 0 to 10, not including 11

"""Nested For Loop

We can write loops inside a loop.

# syntax
for x in y:
    for t in x:
        print(t)"""


person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

for key, value in person.items():
    if key == "address":
        for sub_key, sub_value in value.items():
            print(f"{sub_key}: {sub_value}")

"""For Else

If we want to execute some message when the loop ends, we use else.

# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')"""

for number in range(20):
    print(number)
else:
    print("The loop stops at", number)

"""Pass

In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements."""

for number in range(20):
    pass
