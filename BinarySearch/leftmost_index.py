""" 
Write a function that takes in a sorted list of numbers and a target as arguments. 
The function should return the leftmost index where the target can be found in the list. 
If the target does not exist in the list, then return -1.
Your solution should have a time complexity of O(logn).
"""
from math import floor
def find_leftmost_index(nums: list, target: int):
    low = 0
    high = len(nums) - 1 
    leftmost_index = -1

    while low <= high:
        # calculate mid
        mid = floor((high + low) / 2)
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1 
        else:
            high = mid - 1
            leftmost_index = mid
    return leftmost_index

