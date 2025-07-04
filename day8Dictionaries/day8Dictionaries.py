"""Dictionaries

A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
"""

"""Creating a Dictionary

To create a dictionary we use curly brackets, {} or the dict() built-in function.

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}"""

character = {
    "first_name": "Tulkas",
    "last_name": "UnValar",
    "age": 1000,
    "country": "Mordor",
    "city": "Minas Tirith",
    "alignment": "chaotic good",
    "bonus_characteristics": {
        "str": 3,
        "dex": 2,
        "con": 2,
        "int": 1,
        "wis": 1,
        "cha": 0,
    },
    "saving_throws": {"fortitude": 4, "reflex": 2, "will": 1},
    "hp": 14,
    "ac": 14,
    "speed": 30,
    "init": 2,
    "attacks": {"Melee": "description", "Ranged": "description"},
    "special_abilities": {
        "Fast_movement": "A barbarian’s land speed is faster than the norm for his race by +10 feet",
        "Illiteracy": "Barbarians are the only characters who do not automatically know how to read and write. A barbarian may spend 2 skill points to gain the ability to read and write all languages he is able to speak.",
        "rage": "A  barbarian temporarily gains a +4 bonus to Strength, a +4 bonus to Constitution, and a +2 morale bonus on Will saves, but he takes a -2 penalty to Armor Class",
    },
    "feats": {"Power Attack": "description", "": "description", "": "description"},
    "skills": {
        "climb": 2 + 2,
        "craft": 2 + 2,
        "handle_animal": 2 + 2,
        "intimidate": 0 + 1,
        "jump": 2 + 2,
        "ride": 2 + 2,
        "survival": 2 + 2,
        "swim": 2 + 2,
    },
}
print(character["first_name"])
print(character["last_name"])
print(character["age"])
print(character["country"])
print(character["city"])
print(character["alignment"])
print(character["hp"])
print(character["attacks"]["Melee"])
print(character["special_abilities"])

"""The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary."""

"""Dictionary Length

It checks the number of 'key: value' pairs in the dictionary.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4"""

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
print(len(person))  # 7

print(len(character))

"""Accessing Dictionary Items

We can access Dictionary items by referring to its key name.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4"""

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
print(person["first_name"])  # Asabeneh
print(person["country"])  # Finland
print(person["skills"])  # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person["skills"][0])  # JavaScript
print(person["address"]["street"])  # Space street
# print(person["city"])  # Error

print(character["bonus_characteristics"])

"""Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist."""

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
print(person.get("first_name"))  # Asabeneh
print(person.get("country"))  # Finland
print(
    person.get("skills")
)  # ['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get("city"))  # None

print(character["special_abilities"].get("Illiteracy"))
print(character.get("hd"))

"""Adding Items to a Dictionary

We can add new key and value pairs to a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'"""

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
person["job_title"] = "Instructor"
person["skills"].append("HTML")
print(person)

"""character.append("hd")
print(character)
"""

character["hd"] = 12
print(character["hd"])

"""Modifying Items in a Dictionary

We can modify items in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'"""

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
person["first_name"] = "Eyob"
person["age"] = 252
print(person)

character["bonus_characteristics"]["str"] = 4
print(character["bonus_characteristics"]["str"])

"""Checking Keys in a Dictionary

We use the in operator to check if a key exist in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False"""

print("first_name" in character)
print("first_name" in person)
print("hp" in character)

"""Removing Key and Value Pairs from a Dictionary

pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item"""

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
person.pop("first_name")  # Removes the firstname item
person.popitem()  # Removes the address item
del person["is_married"]  # Removes the is_married item

character.pop("hd")
character.pop("last_name")
del character["city"]
del character["bonus_characteristics"]["dex"]
print(character)

"""Changing Dictionary to a List of Items

The items() method changes dictionary to a list of tuples.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
"""

list_person = person.items()  # Dict items
print(list_person)

"""Clearing a Dictionary

If we don't want the items in a dictionary we can clear them using clear() method

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None"""

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
person.clear()
print(person)

"""Deleting a Dictionary

If we do not use the dictionary we can delete it completely

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct"""

# del person
# print(person)

"""Copy a Dictionary

We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
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

copy_person = person.copy()
print(copy_person)

"""Getting Dictionary Keys as a List

The keys() method gives us all the keys of a a dictionary as a list.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])"""

print(character["bonus_characteristics"].keys())
print(character["skills"].keys())
print(character.keys())

"""Getting Dictionary Values as a List

The values method gives us all the values of a a dictionary as a list.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])"""

print(character["bonus_characteristics"].values())
print(character["skills"].values())
