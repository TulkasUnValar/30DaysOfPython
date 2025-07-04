import math

"""
1. Check the python version you are using"""

"""
2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)
"""

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3**4)
print(3 // 4)

"""3. Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python
"""

print("Mauricio")
print("Quiñones")
print("Colombia")
print("I am enjoying 30 days of python")


"""
4. Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country
"""
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(["Asabeneh", "Python", "Finland"]))
print(type("Mauricio"))
print(type("Quiñones"))
print(type("Colombia"))

"""
Exercise: Level 2
1. Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

Done
"""

"""
Exercise: Level 3
1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

"""

print(type(310))
print(type(3.10))
print(type(3 + 4j))
print(type("Mauricio"))
print(type(True))
print(type([1, 2, 3, 4, 5]))
print(type(("Tulkas", "UnValar")))
print(type({"Mauricio", "Quiñones", "Colombia"}))
print(
    type(
        {
            "strength": "27",
            "dexterity": "20",
            "constitution": "24",
            "intelligence": "18",
            "wisdom": "16",
            "charisma": "18",
        }
    )
)

"""
2. Find an Euclidian distance between (2, 3) and (10, 8)
"""
x1 = 2
y1 = 3
x2 = 10
y2 = 8

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"The Euclidian distance between ({x1}, {y1}) and ({x2}, {y2}) is {d:.2f}")
