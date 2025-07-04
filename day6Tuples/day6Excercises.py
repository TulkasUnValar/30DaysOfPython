"""Exercises: Day 6
Exercises: Level 1"""

# Create an empty tuple

empty_tuple = ()
empty_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ("Vladimir", "Richard")
sisters = ("Sofia", "Mariana")

# Join brothers and sisters tuples and assign it to siblings

siblings = brothers + sisters
print(siblings)

# How many siblings do you have?

print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = list(siblings)
family_members.append("Tulkas")
family_members.append("Galadriel")
print(family_members)
family_members = tuple(family_members)
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings = family_members[0:4]
parents = family_members[4:6]
print(siblings)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("Apple", "Banana", "Mango")
vegetables = ("Cucumber", "Tomato", "Cabbage")
animal_products = ("Milk", "Cheese", "Butter")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

length = len(food_stuff_lt)
middle_index = length // 2
if length % 2 == 1:
    middle_food_stuff_tp = food_stuff_tp[middle_index]
else:
    middle_food_stuff_tp = food_stuff_tp[middle_index - 1 : middle_index + 1]
print(middle_food_stuff_tp)

# Slice out the first three items and the last three items from food_staff_lt list

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(f"First three items: {first_three} and last three items: {last_three}")

# Delete the food_staff_tp tuple completely

del food_stuff_tp
# print(food_stuff_tp)

"""Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')"""

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
