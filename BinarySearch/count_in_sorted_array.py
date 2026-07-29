""" 
Write a function that takes in a sorted list of numbers and a target as arguments. 
The function should return the number of times the target element appears in the list.
Your solution should have a time complexity of O(logn).
"""

from math import floor
def count_in_sorted_array(nums, target):
    low = 0
    high = len(nums) - 1 
    target_left_index = 0
    target_right_index = 0

    while low <= high:
        # calculate mid
        mid = floor((high + low) / 2)
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1 
        else:
            count += 1
    return count
