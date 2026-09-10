""" 
Write a function that takes in a nonnegative integer n as input.
 The function should return the square root of n rounded down to the nearest integer.
You may not use built-in methods like or that trivialize this problem.

Your solution should have a time complexity of O(log(n)).
"""
from math import floor 
def square_root(n):
    high = n
    low = 0

    while low <= high:
        mid = floor((high+low)/2)
        square = mid * mid
        if n < square:
            high = mid - 1 
        elif n > square:
            low = mid + 1 
        else:
            return mid
    return high