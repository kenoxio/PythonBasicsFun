# three commonly used "built in" data structures
# 1. list
# 2. tuple
# 3. dictionary
# a list a sequence of items
# 0-based for indexing
# lists are mutable (they can be changed)
# lists have an order to their items
# -len ... -2 ... -1
# ... 0, 1, 2, 3, 4
nums = [3,6,-1, 7, 9, 7]
print(nums)
print(nums[0], nums[-6], nums[0:2])

# append an item
nums.append(100)
print(nums)
# remove an item
nums.remove(7)
print(nums)

# lists have an order
# means we can sort
print(nums)
nums.sort() # usually from low to high
print(nums)

# 1D lists (line like)
# 2D list (grid like) 
# 3D lists (cube like)
# 4D-nthD lists...

# 2D lists
# there are two main ways to think about 2D lists
# 1. think 2D lists like a 2D table

matrix = [[1, 2, 3,],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[0][0])
print(matrix[1][2])
# 2/ a 1D ;ost wjere eacj ote, os a 1D ;ost (nested lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(matrix[0]))
print(type(matrix[0][0]))

# 3D lists
cube = [[[0, 0],[1, 1]], [2, 2], [3, 3]]
print(cube[0][0][0])

# tuples
# tuples are not mutable/ immutable ( can not be changed )
my_tuple = "x", "y", "z" 
print(my_tuple)
print(type(my_tuple))

# when declaring a single item tuple, you have to have a comma after it
my_single_item_tuple = (1, )
print(my_single_item_tuple)
# to create an empty tuple
my_single_item_tuple = tuple()
print(my_single_item_tuple)

# tuple indexing and slicing is the same as for lists
# tuples are used for returning multiple values

# dictionaries
# a dictionary is a list with keys and indexes and values mapped from those keys
# a key value pair
# use a key to look up a value
# keys in a dictionary must be unique
# examples of a key: student id number
# example of a value: student name
# loop up ID 12345 -> "Jane Doe"
my_dict = {} # empty dictionary
my_empty_dict = dict()
print(my_dict)
my_dict["12345"] = "Jane Doe"
print(my_dict)

state_capitals = {"washington": "olympia", "idaho": "boise", "oregon": "portland"}
print(state_capitals)
# dictionaries are mutable
# you can add key-value pairs as well
state_capitals["california"] = "scaramento"
print(state_capitals)
# the key value pairs can be sorted

# initialize a dict using a list of tuples
roman_numerals = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50)])
print(roman_numerals)
roman_numerals_as_list = list(roman_numerals.items())
print(roman_numerals_as_list)

# types for keys: intergers, strings, files, tuples, etc.
# lists can not be used as keys, because they are mutable while others are not.


# len() works with tuples lists and dictionaries
# lists number of items
print(len(state_capitals))
print("washington" in state_capitals)
print("olympia" in state_capitals.values()) # won't print without .values because olympia is a value
# loops through the key value pairs in a dictionary
for state in state_capitals:
    print(state, state_capitals[state])
for (state, capital) in state_capitals.items(): 
    print(state, "*", capital)