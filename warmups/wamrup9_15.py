#warm up

def has_same_first_last_element(list1, list2):
    same_first = False
    same_last = False

    #check the lists have atleast one element
    if len(list1) > 0 and len(list2) > 0:
        if list1[0] == list2[0]:
            same_first = True
        if list1[-1] == list2[-1]:
            same_last = True
    
    return same_first, same_last

result1, result2, = has_same_first_last_element([1, 2], [1, 3])
print(result1, result2)