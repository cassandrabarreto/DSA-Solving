"""
Write a function, intersection, that takes in two lists, a,b, as arguments.
The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.

"""

def intersection(a, b):
    a = set(a)
    result_list = []

    for i in b:
        if i in a:
            result_list.append(i)
        else:
            continue
    return result_list

print(intersection([4,2,1,6], [3,6,9,2,10]))