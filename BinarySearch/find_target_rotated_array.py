""" 
Write a function that takes in a list of sorted numbers that has been rotated a number of times,
as well as a target element. The function should return the index of the target in the list. 
If the target is not found in the list, then return -1.

Your solution should have a time complexity of O(logn).
You can assume that the input list contains unique elements.    
"""
from math import floor
def find_in_rotated_sorted_array(nums, target):
    low = 0
    high = len(nums) - 1 
    
    while low < high:
        mid = floor((high + low)/ 2 )
            # if mid < high
        if nums[mid] < target:
            # search left inclusive
            high = mid
        else:
            # if mid > high
            # search right exclusive
            low = mid + 1 
    return nums[low]