
""" 
    Write a function that takes in a list of sorted numbers that has been rotated a number of
    times, as well as a target element. The function should return the index of the 
    target in the list. If the target is not found in the list, then return -1.
    Your solution should have a time complexity of O(logn).
    You can assume that the input list contains unique elements.
"""

def find_min_index(nums):
    low = 0
    high = len(nums) - 1 

    while low < high:
        mid = (high + low) // 2
        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid + 1
    return low


def binary_search(nums, target, low, high):

    while low <= high:
        mid = (low + high) // 2

        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return mid
    return -1 

def find_in_rotated_sorted_array(nums, target):
    smallest_index = find_min_index(nums)
    first_half_result = binary_search(nums, target, 0, smallest_index)
    second_half_result = binary_search(nums, target, smallest_index, len(nums) - 1 )

    if first_half_result == - 1:
        return second_half_result
    else:
        return first_half_result