from email import generator
import math
import random


nums = []
for i in range(20):
    rand_num = random.randint(1, 10)
    nums.append(rand_num)
print(nums)

# Prints the numbers all one line, each number separated by a space
for num in nums:
    print(num, end=" ")
print()

# Sorts the list using a list method
nums.sort() # inplace sort
print(nums)
# nums_copy_sorted = sorted(nums) # sorts on copy and returns sorted copy
# print(nums)
# print(nums_copy_sorted)

# Prints the largest and smallest number in the list
# Hint: can you take advantage of the current ordering of your list?
print("min:", nums[0], "max:", nums[-1])
print("min:", min(nums), "max:", max(nums))

# Determines the number of times a user-specified number is in the list
user_input = int(input("Enter a number to count: "))
print("Count:", nums.count(user_input))
# OR
count = 0
for num in nums:
    if num == user_input:
        count += 1
print("Count:", count)

# Removes all instances of a user-specified number in the list. 
# If the number is not in the list print the message: 
# "Sorry, your number is not here!"
user_input = int(input("Enter a number to remove all occurences of: "))
if user_input in nums:
    while user_input in nums:
        nums.remove(user_input)
else:
    print("Sorry, your number is not here!")
print(nums)