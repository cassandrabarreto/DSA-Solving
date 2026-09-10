
""" 
Write a function, binary_search, that takes in a sorted list of numbers and a target.
 The function should return the index where the target can be found within the list. If the 
 target is not found in the list, then return -1.

You may assume that the input array contains unique numbers sorted in increasing order.

Your function must implement the binary search algorithm.

"""
from math import floor

def binary_search(numbers, target):
    high = len(numbers) - 1
    low = 0

    while low <= high:
        # Calculate mid point
        mid = floor((low + high)/2)

        # If target is bigger than mid then move left side ahead
        if target > numbers[mid]:
            low = mid + 1 
        elif target < numbers[mid]:
            high = mid - 1 
        else:
            return mid
    return -1 