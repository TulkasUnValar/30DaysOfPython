"""
Python Error Types

When we write code it is common that we make a typo or some other common error. If our code fails to run, the Python interpreter will display a message, containing feedback with information on where the problem occurs and the type of an error. It will also sometimes gives us suggestions on a possible fix. Understanding different types of errors in programming languages will help us to debug our code quickly and also it makes us better at what we do.

Let us see the most common error types one by one. First let us open our Python interactive shell. Go to your you computer terminal and write 'python'. The python interactive shell will be opened.

SyntaxError
Example 1: SyntaxError

asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
"""

"""As you can see we made a syntax error because we forgot to enclose the string with parenthesis and Python already suggests the solution. Let us fix it.

>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>"""

"""The error was a SyntaxError. After the fix our code was executed without a hitch. Let see more error types."""

"""NameError

Example 1: NameError

>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>"""

"""As you can see from the message above, name age is not defined. Yes, it is true that we did not define an age variable but we were trying to print it out as if we had had declared it. Now, lets fix this by declaring it and assigning with a value."""

""">>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>"""

"""The type of error was a NameError. We debugged the error by defining the variable name."""

"""IndexError

Example 1: IndexError

>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>"""

"""In the example above, Python raised an IndexError, because the list has only indexes from 0 to 4 , so it was out of range."""


"""ModuleNotFoundError

Example 1: ModuleNotFoundError

>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>"""

"""In the example above, I added an extra s to math deliberately and ModuleNotFoundError was raised. Lets fix it by removing the extra s from math.

>>> import math
>>>"""

"""We fixed it, so let's use some of the functions from the math module."""

"""AttributeError

Example 1: AttributeError

>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>"""

"""As you can see, I made a mistake again! Instead of pi, I tried to call a PI function from maths module. It raised an attribute error, it means, that the function does not exist in the module. Lets fix it by changing from PI to pi.

>>> math.pi
3.141592653589793
>>>"""

"""Now, when we call pi from the math module we got the result."""


"""KeyError

Example 1: KeyError

>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>"""

"""As you can see, there was a typo in the key used to get the dictionary value. so, this is a key error and the fix is quite straight forward. Let's do this!

>>> user['country']
'Finland'
>>>"""

"""We debugged the error, our code ran and we got the value."""

"""TypeError
Example 1: TypeError

>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>"""

"""In the example above, a TypeError is raised because we cannot add a number to a string. First solution would be to convert the string to int or float. Another solution would be converting the number to a string (the result then would be '43'). Let us follow the first fix.

>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>"""

"""Error removed and we got the result we expected."""


"""ImportError

Example 1: TypeError


>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>"""

"""There is no function called power in the math module, it goes with a different name: pow. Let's correct it:

>>> from math import pow
>>> pow(2,3)
8.0
>>>"""


"""ValueError

>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>"""

"""In this case we cannot change the given string to a number, because of the 'a' letter in it."""


"""ZeroDivisionError

>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>

We cannot divide a number by zero.

We have covered some of the python error types, if you want to check more about it check the python documentation about python error types. If you are good at reading the error types then you will be able to fix your bugs fast and you will also become a better programmer."""
