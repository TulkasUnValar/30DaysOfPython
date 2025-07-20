import re

# Exercises: Day 18

# Exercises: Level 1

# What is the most frequent word in the following paragraph?

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."


def frequency(paragraph):
    word = paragraph.split()
    frequency = {}
    for i in word:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency


print(frequency(paragraph))


# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

points = ["-12", "-4", "-3", "-1", "0", "4", "8"]
"""sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 - (-12)  # 20
"""


def distance_between_points(points):
    int_points = list(map(int, points))
    sorted_points = sorted(int_points)
    distance = max(sorted_points) - min(sorted_points)
    return distance


print(distance_between_points(points))


# Exercises: Level 2

# Write a pattern which identifies if a string is a valid python variable


def is_valid_variable(variable):
    pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"
    return bool(re.match(pattern, variable))


print(is_valid_variable("first_name"))  # True
print(is_valid_variable("first-name"))  # False
print(is_valid_variable("1first_name"))  # False
print(is_valid_variable("firstname"))  # True

# Exercises: Level 3

# Clean the following text. After cleaning, count three most frequent words in the string.

sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""


def cleaned_text(sentence):
    pattern = r"[@%$&;#!]"
    return re.sub(pattern, "", sentence)


print(cleaned_text(sentence))


def most_frequent_words(paragraph):
    word = paragraph.split()
    frequency = {}
    for i in word:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_frequency[:3]
    return top_3


print(most_frequent_words(cleaned_text(sentence)))
