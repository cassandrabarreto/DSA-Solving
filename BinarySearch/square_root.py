
""" 
Write a function that takes in a nonnegative integer n as input. 
The function should return the square root of n rounded down to the nearest integer.
You may not use built-in methods like or that trivialize this problem.
Your solution should have a time complexity of O(log(n)).
"""

from math import floor
def square_root(n: int) -> int:
    low = 0
    high = n

    while low <= high:
        # calculate mid
        mid = floor((low + high)/2)
        mid_square = mid * mid
        if n < mid_square:
            high = mid - 1
        elif n > mid_square:
            low = mid + 1
        else:
            return mid
    # high pointer is lower than low pointer outside of the loop. (square root of n rounded down )
    return high