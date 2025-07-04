import math

# Exercises

# Declare your age as integer variable
age = 450

# Declare your height as a float variable
height = 1.78
# Declare a variable that store a complex number
complex_num = 3 + 4j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

"""Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)."""
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(
    f"The area of the rectangle is {area_rectangle}, the perimeter is {perimeter_rectangle}"
)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radio = float(input("Enter the radius of the circle: "))
area_of_circle = 3.1416 * (radio**2)
circumference_of_circle = 2 * 3.1416 * radio
print(
    f"The area of the circle is {area_of_circle}, the circumference is {circumference_of_circle}"
)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2  # slope

x1 = 0
y1 = 2 * x1 - 2

y2 = 0
x2 = (y2 + 2) / 2
print(f"Point 1 ({x1}, {y1}), Point 2 ({x2}, {y2})")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10

m2 = (y2 - y1) / (x2 - x1)
print(f"The slope (m) between points ({x1}, {y1}) and ({x2}, {y2}) is {m:.2f}")

Euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(
    f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {Euclidean_distance:.2f}"
)

# Compare the slopes in tasks 8 and 9.
print(m == m2)  # Should be False since they are different lines
print(m != m2)  # Should be True since they are different lines

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x**2 + 6 * x + 9
print(f"when x = {x}, y = {y}")

x1 = -1
y = x1**2 + 6 * x1 + 9
print(f"when x = {x1}, y = {y}")

x2 = 0
y = x2**2 + 6 * x2 + 9
print(f"when x = {x2}, y = {y}")

x3 = 1
y = x3**2 + 6 * x3 + 9
print(f"when x = {x3}, y = {y}")

x4 = 3
y = x4**2 + 6 * x4 + 9
print(f"when x = {x4}, y = {y}")

x5 = 5
y = x5**2 + 6 * x5 + 9
print(f"when x = {x5}, y = {y}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") == len("dragon"))
print(len("python") != len("dragon"))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")

# There is no 'on' in both dragon and python
print("on" not in "python" and "on" not in "dragon")

# Find the length of the text python and convert the value to float and convert it to string
python_length_float = float(len("python"))
python_length_str = str(python_length_float)
print(
    f"Length of 'python' as float: {python_length_float}, as string: {python_length_str}"
)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = 2
if num % 2 == 0:
    print(f"{num} in an even number")
else:
    print(f"{num} is not an even number")

print(2 % 2 == 0)  # True, because 2 is even

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))  # True, because 7 // 3 is 2 and int(2.7) is also 2

# Check if type of '10' is equal to type of 10
print(type("10") == type(10))

# Check if int('9.8') is equal to 10
print(int(float("9.8")) == 10)  # False, because int('9.8') will raise an error


"""Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
  Enter hours: 40
  Enter rate per hour: 28
  Your weekly earning is 1120"""
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours * rate_per_hour}")

""" Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
"""
years = float(input("Enter number of years: "))
seconds_per_years = 365 * 24 * 60 * 60  # Average number of seconds in a year
print(f"You have lived for {years * seconds_per_years} seconds")

"""Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125"""

for i in range(1, 6):
    row = [str(i)]
    for j in range(4):
        row.append(str(i**j))
    print(" ".join(row))

print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 25\n4 1 4 16 64\n5 1 5 25 125")

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

"""for i in range(1, 6):
    row = [str(i) "1", str(i), str(i**2), str(i**3)]
    print(" ".join(row))"""

print(math.factorial(1))
print(math.factorial(2))
print(math.factorial(3))
print(math.factorial(4))
print(math.factorial(5))
