"""     
Write a function that takes in a sorted list of numbers and a target as arguments. 
The function should return the number of times the target element appears in the list.
Your solution should have a time complexity of O(logn).
"""
from math import floor
def count_in_sorted_array(nums, target):
    leftmost = find_leftmost_index(nums,target)
    rightmost = find_rightmost_index(nums,target)
    rightmost - leftmost + 1 

    if rightmost == -1:
        return 0
    else:
        return rightmost - leftmost + 1

def find_leftmost_index(nums, target):
    high = len(nums) - 1 
    low = 0
    leftmost = -1

    while low <= high:
        mid = floor((high+low)/2)
        if target < nums[mid]:
            high = mid - 1 
        elif target > nums[mid]:
            low = mid + 1 
        else:
            high = mid - 1 
            leftmost = mid
    return leftmost


def find_rightmost_index(nums, target):
    high = len(nums) - 1 
    low = 0
    rightmost = -1

    while low <= high:
        mid = floor((high+low)/2)
        if target < nums[mid]:
            high = mid - 1 
        elif target > nums[mid]:
            low = mid + 1 
        else:
            low = mid + 1 
            rightmost = mid
    return rightmost