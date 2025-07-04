# Exercises: Day 8

# Create an empty dictionary called dog

dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "buster"
dog["color"] = "grey"
dog["breed"] = "bull terrier"
dog["legs"] = 4
dog["age"] = 3

print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {}
student["first_name"] = "Barajir"
student["last_name"] = "Iron fist"
student["gender"] = "male"
student["age"] = "16"
student["marital_status"] = "single"
student["skills"] = [
    "Craft",
    "Arcane Knowledge",
    "Balance",
    "Concentration",
    "Diplomacy",
    "Escape Artist",
    "Hide",
    "Listen",
    "Perform",
    "Sense Motive",
    "Swim",
    "Trade",
    "Tricks",
    "Religious Knowledge",
]
student["country"] = "Valinor"
student["city"] = "Cracoa"
student["address"] = "Iron Fist home"

# Get the length of the student dictionary

print(len(student))

# Get the value of skills and check the data type, it should be a list

print(type(student["skills"]))

# Modify the skills values by adding one or two skills

student["skills"].append("Climb")
student["skills"].append("Jump")
print(student["skills"])

# Get the dictionary keys as a list

student_keys = list(student.keys())
print(student_keys)
print(type(student_keys))

# Get the dictionary values as a list

student_values = list(student.values())
print(student_values)
print(type(student_values))

# Change the dictionary to a list of tuples using items() method

list_of_tuples = list(student.items())
print(list_of_tuples)

# Delete one of the items in the dictionary
del student["country"]
print(student)

# Delete one of the dictionaries
del dog
# print(dog)
