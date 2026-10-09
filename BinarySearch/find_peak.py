""" 

    Write a function that takes in a list of numbers. 
    The function should return the index of a "peak" element.
    A "peak" is an element that is greater than both of its adjacent neighbors. 
    If there are multiple peaks, you may return the index of any one of them.

    Note that the first and last elements of the list only need to be greater than their single ]
    neighbor to be considered a "peak".

    Your solution should have a time complexity of O(logn).
    You can assume that adjacent numbers of the list are not equal.

"""

def find_peak(nums):
    # Initialize pointers
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (high + low ) // 2

        # Check if uphill is left or right
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return high