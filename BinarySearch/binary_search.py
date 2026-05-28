""" 
Write a function, binary_search, that takes in a sorted list of numbers and a target. 
The function should return the index where the target can be found within the list. 
If the target is not found in the list, then return -1.

You may assume that the input array contains unique numbers sorted in increasing order.

Your function must implement the binary search algorithm.
"""
from math import floor
def binary_search(numbers: list[int], target: int) -> int :
    low = 0
    high = len(numbers) - 1 

    while low <= high:
        # calculate mid point
        mid = floor(low + high)
        # Check if target is greater or smaller than mid_point
        if target < numbers[mid]:
            #shift high to left
            high = mid - 1
        elif target > numbers[mid]:
            # shift low to right
            low = mid + 1
        else:
            # if i and j are the same, return mid
            return mid
    return -1