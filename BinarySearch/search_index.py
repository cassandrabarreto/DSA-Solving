""" 
Write a function that takes in a sorted list of numbers and a target. 
The function should return the index where the target can be found within the list. 
If the target is not found in the list, then return the index where it should appear in the sorted order.
You may assume that the input list contains unique numbers sorted in increasing order.

Your solution should have a runtime of O(logn).    

"""
from math import floor
def binary_search_index(nums: list, target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = floor((low + high)/2)
        if target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            return mid
    return low


