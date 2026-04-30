""" 
Write a function that takes in a list of numbers and a size k as arguments. 
The function should return the maximum product of subarrays that contain exactly k elements.
You can assume that k is less than or equal to the length of the input list.
You can assume that numbers of the list are non-zero.
"""

import math

def max_subarray_product_size_k(nums, k):
    # process first window
    current_prod = math.prod(nums[:k])

    # Calculate max_prod
    max_prod = current_prod

    # Start iterating to shift window
    for i in range(0, len(nums) - k):
        current_prod /= nums[i]
        current_prod *= nums[i+k]
        max_prod = max(current_prod, max_prod)
    return max_prod

