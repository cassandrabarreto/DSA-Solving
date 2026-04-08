""" 
    Write a function, palindrome, that takes in a string and returns a boolean indicating whether or 
    not the string is the same forwards and backwards.

"""

def palindrome(s):
    if s[0] != s[:-1]:
        return False
    if len(str) == 1 or s == "":
        return True
    return palindrome(s[1:-1])