# Operators

"""
Boolean
A boolean data type represents one of the two values: True or False. The use of these data types will be clear once we start using the comparison operator. The first letter T for True and F for False should be capital unlike JavaScript. Example: Boolean Values
"""

print(True)
print(False)

"""Operators

Python language supports several types of operators. In this section, we will focus on few of them.
  """

"""Assignment Operators

Assignment operators are used to assign values to variables. Let us take = as an example. Equal sign in mathematics shows that two values are equal, however in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable. The table below shows the different types of python assignment operators, taken from w3school: https://www.w3schools.com/python/python_operators.asp."""

"""
Operator	Example	    Same As
=	        x = 5	      x = 5	
+=	      x += 3	    x = x + 3	
-=	      x -= 3	    x = x - 3	
*=	      x *= 3	    x = x * 3	
/=	      x /= 3	    x = x / 3	
%=	      x %= 3	    x = x % 3	
//=	      x //= 3	    x = x // 3	
**=	      x **= 3	    x = x ** 3	
&=	      x &= 3	    x = x & 3	
|=	      x |= 3	    x = x | 3	
^=	      x ^= 3	    x = x ^ 3	
>>=	      x >>= 3	    x = x >> 3	
<<=	      x <<= 3	    x = x << 3	
:=	  print(x := 3)	  x = 3 print(x)"""

"""Arithmetic Operators:
Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b
Exponentiation(**): a ** b"""

# Arithmetic Operations in Python
# Integers

print("Addition: ", 1 + 2)  # 3
print("Subtraction: ", 2 - 1)  # 1
print("Multiplication: ", 2 * 3)  # 6
print("Division: ", 4 / 2)  # 2.0  Division in Python gives floating number
print("Division: ", 6 / 2)  # 3.0
print("Division: ", 7 / 2)  # 3.5
print(
    "Division without the remainder: ", 7 // 2
)  # 3,  gives without the floating number or without the remaining
print("Division without the remainder: ", 7 // 3)  # 2
print("Modulus: ", 3 % 2)  # 1, Gives the remainder
print("Exponentiation: ", 2**3)  # 9 it means 2 * 2 * 2

# Floating numbers
print("Floating Point Number, PI", 3.14)
print("Floating Point Number, gravity", 9.81)

# Complex numbers
print("Complex number: ", 1 + 1j)
print("Multiplying complex numbers: ", (1 + 1j) * (1 - 1j))

"""Let's declare a variable and assign a number data type. I am going to use single character variable but remember do not develop a habit of declaring such types of variables. Variable names should be all the time mnemonic."""

# Declaring the variable at the top first

a = 3  # a is a variable name and 3 is an integer data type
b = 2  # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
sum = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
exp = a**b
floor_division = a // b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions

print("Sum: ", sum)  # 5
print("Difference: ", diff)  # 1
print("Product: ", product)  # 6
print("Division: ", division)  # 1.5
print("Remainder: ", remainder)  # 1
print("Exponentiation: ", exp)  # 8
print("Floor Division: ", floor_division)  # 1

print("== Addition, Subtraction, Multiplication, Division, Modulus ==")

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print("total: ", total)
print("difference: ", diff)
print("product: ", product)
print("division: ", div)
print("remainder: ", remainder)

"""Let us start start connecting the dots and start making use of what we already know to calculate (area, volume,density, weight, perimeter, distance, force)."""

# Calculating area of a circle
radius = 10  # radius of a circle
area_of_circle = 3.14 * radius**2  # two * sign means exponent or power
print("Area of a circle:", area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("Area of rectangle:", area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, "N")  # Adding unit to the weight

# Calculate the density of a liquid
mass = 75  # in Kg
volume = 0.075  # in cubic meter
density = mass / volume  # 1000 Kg/m^3
print("Density of the liquid:", density, "Kg/m^3")

"""Comparison Operators

In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. The following table shows Python comparison operators which was taken from w3shool: https://www.w3schools.com/python/python_operators.asp."""


"""
Operator	      Name	       Example
==	            Equal	        x == y	
!=	            Not equal	    x != y	
>	              Greater than	x > y	
<	              Less than	    x < y	
>=	  Greater than or equal to	x >= y	
<=	  Less than or equal to	  x <= y"""

print(3 > 2)  # True, because 3 is greater than 2
print(3 >= 2)  # True, because 3 is greater than 2
print(3 < 2)  # False,  because 3 is greater than 2
print(2 < 3)  # True, because 2 is less than 3
print(2 <= 3)  # True, because 2 is less than 3
print(3 == 2)  # False, because 3 is not equal to 2
print(3 != 2)  # True, because 3 is not equal to 2
print(len("mango") == len("avocado"))  # False
print(len("mango") != len("avocado"))  # True
print(len("mango") < len("avocado"))  # True
print(len("milk") != len("meat"))  # False
print(len("milk") == len("meat"))  # True
print(len("tomato") == len("potato"))  # True
print(len("python") > len("dragon"))  # False


# Comparing something gives either a True or False

print("True == True: ", True == True)
print("True == False: ", True == False)
print("False == False:", False == False)

"""In addition to the above comparison operator Python uses:

is: Returns true if both variables are the same object(x is y)
is not: Returns true if both variables are not the same object(x is not y)
in: Returns True if the queried list contains a certain item(x in y)
not in: Returns True if the queried list doesn't have a certain item(x in y)"""

print("1 is 1", 1 is 1)
print("1 is not 1", 1 is not 1)
print("a in Tulkas", "a" in "Tulkas")
print("U in Tulkas", "U" in "Tulkas")
print("m is not in Tulkas", "m" not in "Tulkas")
print("coding" in "coding for all")
print("4 is 2 ** 2", 4 is 2**2)

"""Logical Operators

Unlike other programming languages python uses keywords and, or and not for logical operators. Logical operators are used to combine conditional statements:"""

"""
Operator	                              Description	                                      Example
and 	                  Returns True if both statements are true	                        x < 5 and  x < 10	
or	                    Returns True if one of the statements is true	                    x < 5 or x < 4	
not	                    Reverse the result, returns False if the result is true	          not(x < 5 and x < 10)"""

print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print("True and True: ", True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print("True or False:", True or False)
print(not 3 > 2)  # False - because 3 > 2 is true, then not True gives False
print(not True)  # False - Negation, the not operator turns true to false
print(not False)  # True
print(not not True)  # True
print(not not False)  # False
