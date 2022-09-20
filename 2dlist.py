from email import generator
from fcntl import F_SEAL_SEAL
import math
import random




table = []

for i in range(10):
    # build a row
    row = []
    for j in range(5):
        # gen ran num
        rand_num = random.randrange(1,11)
        row.append(rand_num)
    table.append(row)
print(table)

for row in table:
    for num in row:
        print(num, end="\t")
    print()

curr_min = curr_max = table[0][0]
for row in table:
    for value in row:
        if value < curr_min:
            curr_min = value
        if value > curr_max:
            curr_max = value
print("min:", curr_min, "max:", curr_max)

user_input = int(input("Enter a number to count: "))
count = 0
for row in table:
    for num in row:    
        if num == user_input:
            count += 1
print("Count:", count)

user_input = int(input("Enter a number between 1 and 10:"))

removed = False
for row in table: 
    while user_input in row:
        row.remove(user_input)
        removed = True
if not removed:
    print("Your number is either not in the list, or is not inbetween 1 and 10")
print(table)


list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
list3[0] = 200
# List 3 is not a copy of list 1, but just an alias for list1

def add_one_to_each_element(some_list):
    # some_list is just another alias for list1, just like list3
    for i in range(len(some_list)):
        some_list[i] += 1

add_one_to_each_element(list3)
print(list1, list2, list3)

# python is "pas by object reference"
# if you pass a list to a function, code in that
# function can modify the list in memory

#more on  stirngs
word = "gonzaga"
print(word[0], word[-1], word[2:4])
# strings are immutable (can not be changed)
wprd = "G" + word[1:]
print(word)
print((word, end = "\n") * 5)