"""
Write a function, is_palindrome, that takes in a string and returns a boolean 
indicating whether or not the string is the same forwards and backwards.
"""
# Non-efficient Version
def is_palindrome(s):
    reverse_word = s[::-1]

    if reverse_word == s:
        return True
    else:
        return False
    
# Efficient Version with Two Pointers
def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
    