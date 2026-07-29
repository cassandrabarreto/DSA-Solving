""" 
Write a function that takes in a list of sorted numbers that has been rotated a number of times.
The function should return the minimum element of the list.

Your solution should have a time complexity of O(logn).

You can assume that the numbers of the input list are unique.    
"""
from math import floor
def min_in_rotated_sorted_array(nums):
    low = 0
    high = len(nums) - 1 
    mid = -1

    while low < high:
        mid = floor((high + low)/ 2 )
        # if mid < high
        if nums[mid] < nums[high]:
            # search left inclusive
            high = mid
        else:
            # if mid > high
            # search right exclusive
            low = mid + 1 
    return nums[low]
