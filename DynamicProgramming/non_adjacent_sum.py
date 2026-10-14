""" 
    Write a function, non_adjacent_sum, that takes in a list of numbers as an argument. 
    The function should return the maximum sum of non-adjacent items in the list. 
    There is no limit on how many items can be taken into the sum as long as they are not adjacent.
    You can assume that the numbers are nonnegative.

    For example, given:

    [2, 4, 5, 12, 7]

    The maximum non-adjacent sum is 16, because 4 + 12. 
    4 and 12 are not adjacent in the list.
"""

def non_adjacent_sum(nums):
    return _non_adjacent_sum_helper(nums, 0, {})

def _non_adjacent_sum_helper(nums, i, memo):
    if i in memo:
        return memo[i]
    # If len of list is 0, return 0
    if i >= len(nums):
        return 0

    # include number option
    include = nums[i] + _non_adjacent_sum_helper(nums, i + 2, memo)
    
    # exclude number option
    exclude = _non_adjacent_sum_helper(nums, i + 1, memo)

    memo[i] = max(include, exclude)
    return memo[i]