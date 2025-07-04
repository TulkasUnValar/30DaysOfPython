"""Exercises: Day 9

Exercises: Level 1"""

"""Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive."""

age = int(input("Enter your age: "))  # Get user input
needed_age = 18

if age >= needed_age:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {needed_age - age} more years to learn to drive.")

"""Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me."""

age1 = int(input("Enter my age: "))
age2 = int(input("Enter your  age: "))

if age1 > age2:
    if age1 - age2 == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age1-age2} years older than you.")
elif age1 < age2:
    if age2 - age1 == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age2-age1} years older than me.")
else:
    print("We have the same age.")

"""Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3"""

num_one = int(input("Enter number one: "))
num_two = int(input("Enter number two: "))

if num_one > num_two:
    print(f"{num_one} is greater than {num_two}")
elif num_one < num_two:
    print(f"{num_one} is smaller than {num_two}")
else:
    print(f"{num_one} is equal to {num_two}")

# Exercises: Level 2

"""Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F"""

score = int(input("Enter the student score (between 0 and 100): "))
if score >= 80 and score <= 100:
    print("A")
elif score >= 70 and score <= 89:
    print("B")
elif score >= 60 and score <= 69:
    print("C")
elif score >= 50 and score <= 59:
    print("C")
elif score >= 0 and score <= 89:
    print("F")
else:
    print("Invalid score")

"""Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer"""

input_month = input("Enter the month: ")
month = input_month.lower()
if month == "march" or month == "april" or month == "may":
    print("Sprint")
elif month == "june" or month == "july" or month == "august":
    print("Summer")
elif month == "september" or month == "october" or month == "november":
    print("Autumn")
elif month == "december" or month == "january" or month == "february":
    print("Winter")
else:
    print("Invalid month")


"""The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""

fruits = ["banana", "orange", "mango", "lemon"]

input_fruit = input("Enter a fruit: ")
formatted_fruit = input_fruit.lower()
if formatted_fruit not in fruits:
    fruits.append(formatted_fruit)
    print(fruits)
else:
    print("That fruit already exist in the list")

# Exercises: Level 3

"""Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
"""

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

skills = person["skills"]
"""print(type(skills))"""
length = len(skills)
"""print(length)
print(person.keys())"""
middle_index = length // 2
"""print(middle_index)
print(skills[middle_index])"""

if "skills" in person.keys():
    print(skills[middle_index])
else:
    print("No skills")


# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

skills = person["skills"]
if "skills" in person.keys():
    if "Python" in skills:
        print("Python is in the skills")
    else:
        print("Python is not in the skills")
else:
    print("No skills")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

skills = person["skills"]

if skills == {"JavaScript", "React"}:
    print("He is a front end developer")
elif "React" in skills and "Node" in skills and "MongoDB" in skills:
    print("He is a fullstack developer")
elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
    print("He is a backend developer")
else:
    print("unknown title")

"""if skills == {"JavaScript", "React"}:
    print("He is a front end developer")
elif skills == {"Node", "Python", "MongoDB"}:
    print("He is a backend developer")
elif skills == {"React", "Node", "MongoDB"}:
    print("He is a fullstack developer")
else:
    print("unknown title")"""

# If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.

if person["is_married"] and person["country"] == "Finland":
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married."
    )
else:
    print("unknown")
