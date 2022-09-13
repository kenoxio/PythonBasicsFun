import math

# this is a one line comment askldjfaskldj
# a comment is used to document your code
# comments are ignored by python

"""
this is a multi
line comment
AKA block comment
"""

# game plan:
# 1. variables
# 2. operators
# 3. getting input from theuser
# 4. formatting decimal numbers


# VARIABLES 
# a variable stores a value
from re import X


x = 5 # x is a variable which is storing the value.
# x is not EQUAL to five, but it is just a box holding five.
# the value 5 is an interger (int for short)
print(x)
# we can check the type of x
# the data type represents the range of values
print(type(x))
# we can reassign x

x = 5.5 # this is not a value anymore, it is a float
# a number with a fractional part
print(x)
print(type(x))

x = "hello1234"
# this represents a string (str) value, another data type
# a sequence of characters
print(x)
print(type(x))

# OPERATORs
# PEMDAS - Parenthesis(), exponents**, multiplication*, division (/, //, %), addition+, subtraction-.
# +, -
# * is multiplicaion
print(4 * 5)
# / is a floating point division (like "normal" division)
print(4 / 12)
# // is integer division (is the whole number result of floating point division)
print(4 // 12)
# % is the modulus operator (is the remainder of interger division)
print(9 % 5)
# ** is the exponentiation operator (power)
print(5 ** 2)


# warm up
# print(3.0 % 1)
# print (3 / 0)
# print(2 ** 4 ** (2/4))
print (math.pow(5,2))
print("Enter your favorite number: ")
fav_num = input()
print(type(fav_num))
print("Your favorite number doubled is", 2 * fav_num)
# we often need to convert between types
# type conversion

# DECIMAL FORMATTING
# there a LOTS of ways to do this.
print(math.pi)
print("%.2f" %(math.pi))
print("{:.2f}".format(math.pi))
print(f"{math.pi:.2f}")
print(round(math.pi, 2))

#conditionals AKA if statements
#if some condition (boolean condition) is true
#then execute some code
x = 5
if x == 5: # == is the equality operator
    print("hello")
    # python uses indentation (1 tab = 4 spaces)
    # to group code together into "blocks"
    # like {} C/C++
