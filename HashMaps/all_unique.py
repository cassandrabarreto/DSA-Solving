""" 
    Write a function, all_unique, that takes in a list. 
    The function should return a boolean indicating whether or not
    the list contains unique items.
"""

def all_unique(items):
    
    set_version = set(items)

    if len(set_version) == len(items):
        return True
    else:
        return False



all_unique(["q", "r", "s", "a"]) # -> True
all_unique(["cat", "cat", "dog"])
