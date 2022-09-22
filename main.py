from email.utils import collapse_rfc2231_value
import math, random
from operator import itemgetter

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
#print("Enter your favorite number: ")
#fav_num = input()
#print(type(fav_num))
#print("Your favorite number doubled is", 2 * fav_num)
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

# we also have an else keyword
# else executes when preceding if condition is false
if x == 7:
    print("x = 5")
else:
    print("x =/= 5")

# we also have an elif (else if) keyword
# use elif when you want ot test multiple conditions in a row
x = -2
if x < 0:
    print("x is negative")
elif x > 0:
    print("x is postive")
else:
    print("x = 0")

# you can nest if statements (put an if inside another if)
# be aware of indentation

# LOOPS
# use a loop when you want to repeat code
# in python we have for loops and whiel loops
# for loop sturcutre
# for item in sequence:
#   body of for loop (code if you want repeated)
for item in [3, 5, 7, "hello"]:
    print(item)
for letter in "slalom":
    print(letter)
# we can also make our own sequence using range()
# range(stop) # [0, stop)
for i in range(9):
    print(i, end=" ")
print()

# range(start, stop) # [start, stop)
for i in range(4, 9):
    print(i, end=" ")
print()

# range(start, stop, step) # [start, stop) up by step
for i in range(4, 9, 2):
    print(i, end=" ")
print()

# task: write a for loop to print 8 6 4
# task: write a for loop to print the first 20 even numbers
for i in range(8, 2, -2):
    print(i, end=" ")
print(4)
for i in range(2, 40, 2):
    print(i, end=", ")
print(i + 2)

# ADVANCED LOOPs
# like if statements you can nest loops
# we can get an early exit from a loop with the break keyword
# while loops
# whie loops structure
# while condition is true:
#   body of loop(code to repeated)
#   progress towards condition being false
# while True:
#    user_input = input("enter a word(stop to exit): ")
#    if user_input == "stop":
#        break # early exit 

# task: rewrite the first 20 even # code to use a while loop instead of a for loop
k = 2
while k <= 38:
    print(k, end=", ")
    k += 2 #progress towards k > 38
print(k)

# FUNCTIONs
# a named sequence of satements
# we have been using functions: math.pow(), print(), sorted(), len()
# int(), range(), input()
# functions accept input (argyments when you "call" the function)
# parameters when you "define" the function
# functions produce output (return values aka results)
# function structure
# def function_name(parameter list):
#   function body (statements to be executed
#   when this function is "called")

# example 1: a function with no inputs (no arguments when you call it)
# and no outputs
def say_hello():
    print("hello")
say_hello()
for i in range(5):
    say_hello()

# example 2: a function with one inputs (one arugments when yo call it)
# and no outputs
def say(message):
    print("message:", message)
say("yo yo") # function call)

# task: define/call function that accepts a radius of a circle
# and prints the circles area

# RANDOM NUMBER
# often we need random numbers to simulate random events 
# or initializing the state of an algorithm

# if you want the same random numbers each time you run
# your program, "seed" the random number generator
random.seed(0)

# lets roll a 6 sided die
# import the random module
roll = random.randrange(1, 101) # [1, 7)
print("Rolled number:",roll)
if roll == [1]:
    print("YOU WON!")
else:    
    print("Try again!")

cars = ["Corolla", "Lamborghini", "Skyline GTR R34", "Koenigsegg"]
cars.append("Mercedes AMG")
print(cars)
# extend
cars.extend(["Legacy", "Jaguar"])
print(cars)
# +=
cars += ["Forester", "Accord"]
print(cars)
cars2 = ["Ghost", "Jesko"]
cars += cars2
print(cars)

#removed a car in the list through pop (position)
cars.pop(0)
print(cars)

#create a string from a list of strings
word_list = ["*", "c", "or", "o", "lla", "*"]
word_str = "".join(word_list)
print(word_str)
word_list2 = list(word_str)
print(word_list2)
comma_seperated_value_str = "c,or,o,lla"
word_list3 = comma_seperated_value_str.split(",")
print(word_list3)

# String methods
# like join (), Split()
# strip()
word = "    \n \t\t    hello   \n\n\t  "
print(repr(word))
word = word.strip()
print(repr(word))
# find()
print(word.find("ll"))
# it prints 2, which is the position of where it starts
print (word.find("zz")) 
