""" 
    Write a function, factorial, that takes in a number n and returns the factorial of that number. 
    The factorial of n is the product of all the positive numbers less than or equal to n. 
    You must solve this recursively.
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)