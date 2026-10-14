""" 
    
    Write a function, summing_squares, that takes a target number as an argument. 
    The function should return the minimum number of perfect squares that sum to the target. 
    A perfect square is a number of the form (i*i) where i >= 1.

    For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.

    Given 12:

    summing_squares(12) -> 3

    The minimum squares required for 12 is three, by doing 4 + 4 + 4.

    Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.
"""
from math import sqrt , floor

def summing_squares(n):
    pass

def summing_squares_helper(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    min_squares = float('inf')

    for i in range(1, floor(sqrt(n) + 1)):
        square = i * i
        num_squares = 1 + summing_squares(n - square, memo)
        min_squares = min(min_squares, num_squares)
    memo[n] = min_squares
    return min_squares