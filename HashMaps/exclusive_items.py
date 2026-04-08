""" 
Write a function, exclusive_items, that takes in two lists, a,b, as arguments.
The function should return a new list 
containing elements that are in either list but not both lists.

You may assume that each input list does not contain duplicate elements.
"""

def exclusive_items(a, b):
    new_list = []
  
    a = set(a)

    b = set(b)

    for i in b:
        if i in a:
            continue
        else:
            new_list.append(i)

    for i in a:
        if i in b:
            continue
        else:
            new_list.append(i) 
    return new_list

exclusive_items([4,2,1,6], [3,6,9,2,10]) # -> [4,1,3,9,10]