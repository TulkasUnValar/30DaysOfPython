import myModule
from myModule import full_name, sum_two_nums, weight, person
from myModule import full_name as fn, sum_two_nums as st, weight as w, person as p
import os
import sys
from statistics import *  # importing all the statistics modules
import math
from math import pi
from math import pi, sqrt, pow, floor, ceil, log10
from math import *
from math import pi as PI
import string
from random import random, randint


print(myModule.full_name("Tulkas", "UnValar"))

print(full_name("Bauglir", "Hatrasil"))

print(sum_two_nums(10, 20))

print(weight(100))

print(person["country"])
print(person["city"])


print(fn("Bauglir", "Hatrasil"))

print(st(10, 20))

print(w(100))

print(p)
print(p["country"])
print(p["city"])


ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))  # ~22.9
print(median(ages))  # 23
print(mode(ages))  # 20
print(stdev(ages))  # ~2.3

print(math.pi)  # 3.141592653589793, pi constant
print(math.sqrt(2))  # 1.4142135623730951, square root
print(math.pow(2, 3))  # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))  # 10, rounding to the highest
print(math.log10(100))  # 2, logarithm with 10 as base

print(pi)

print(pi)  # 3.141592653589793
print(sqrt(2))  # 1.4142135623730951
print(pow(2, 3))  # 8.0
print(floor(9.81))  # 9
print(ceil(9.81))  # 10
print(log10(100))  # 2

print(PI)  # 3.141592653589793


print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.hexdigits)  # 0123456789abcdefABCDEF
print(string.octdigits)  # 01234567
print(string.printable)  # all printable characters
print(string.whitespace)  # space, tab, newline, etc.
print(string.capwords("hello world"))  # Hello World

print(
    random()
)  # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20))  # it returns a random integer number between [5, 20] inclusive
