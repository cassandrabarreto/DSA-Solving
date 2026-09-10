
""" 
    Write a function that takes in a list of sorted numbers that has been rotated a number of times, 
    as well as a target element. The function should return the index of the target in the list. 
    If the target is not found in the list, then return -1.
    Your solution should have a time complexity of O(logn).
    You can assume that the input list contains unique elements.    
"""

def find_in_rotated_sorted_array(nums, target):
    high = len(nums) - 1 
    low = 0 

    while low <= high:
        mid = (low + high) // 2 

        if target < nums[mid]:
            low = mid + 1 
        if target > nums[mid]:
            high = mid - 1 
