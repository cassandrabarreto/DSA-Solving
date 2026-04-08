""" 
    Write a function, reverse_string, that takes in a string as an argument. 
    The function should return the string with its characters in reverse order. 
    You must do this recursively.
"""

def reverse_string(s):
    if s == "":
        return ""
    return s[-1] + s[:-1]