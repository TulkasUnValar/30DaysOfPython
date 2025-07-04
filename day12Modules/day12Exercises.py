import random
import string
from random import choice, randint, sample, shuffle, uniform, randrange, random

# Exercises: Level 1

"""Write a function which generates a six digit/character random_user_id.
print(random_user_id());
'1ee33d'"""


def random_user_id():
    user_id = []
    letters = string.ascii_letters
    digits = string.digits
    characters = letters + digits
    for _ in range(6):
        user_id.append(choice(characters))
    return "".join(user_id)


print(random_user_id())


def random_user_id():
    characters = string.ascii_letters + string.digits
    return "".join(choice(characters) for _ in range(6))


print(random_user_id())

"""Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr"""


def random_user_id(length, count):
    characters = string.ascii_letters + string.digits
    passwords = []
    for _ in range(count):
        password = "".join(choice(characters) for _ in range(length))
        passwords.append(password)
    return passwords


print(random_user_id(4, 8))
print(random_user_id(8, 5))
print(random_user_id(20, 4))

"""Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
"""


def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f"rgb({r},{g},{b})"


print(rgb_color_gen())

# Exercises: Level 2

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).


def list_of_hex_colors(count):
    hex = string.hexdigits.lower()
    hex_colors = []
    for _ in range(count):
        color = "#" + "".join(choice(hex) for _ in range(6))
        hex_colors.append(color)
    return hex_colors


print(list_of_hex_colors(7))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.


def list_of_rgb_colors(count):
    rgb_colors = []
    for _ in range(count):
        color = f"rgb(({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)}))"
        rgb_colors.append(color)
    return rgb_colors


print(list_of_rgb_colors(5))

"""Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']"""


def generate_colors(color_type, count):
    if color_type == "hex":
        return list_of_hex_colors(count)
    elif color_type == "rgb":
        return list_of_rgb_colors(count)
    else:
        return "Invalid color type. Please use 'hex' or 'rgb'."


print(generate_colors("hex", 6))
print(generate_colors("rgb", 6))
print(generate_colors("hex", 9))
print(generate_colors("rgb", 9))

# Exercises: Level 3

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list


def shuffle_list(list):
    shuffle_list = list.copy()
    shuffle(shuffle_list)
    return shuffle_list


number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(shuffle_list(number))

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


def set_seven_random_numbers():
    numbers = set()
    while len(numbers) < 7:
        numbers.add(randint(0, 9))
    return list(numbers)


print(set_seven_random_numbers())
