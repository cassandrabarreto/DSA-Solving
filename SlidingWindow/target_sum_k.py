""" 
    Write a function that takes in a list of numbers, a target sum, 
    and a size k as arguments. The function should return the number 
    of subarrays of size k that sum to the target.
    You can assume that k is less than or equal to the length of the input list.
"""

def subarray_target_sum_size_k(nums: list, target: int, k: int) -> int:
    # First Window Processing
    current_value = sum(nums[:k])
    count = 0

    count = 1 if current_value == target else 0

    for i in range(0, len(nums) - k):
        # remove trailing element
        current_value -= nums[i]
        # add up leading element
        current_value += nums[i + k]

        if current_value == target:
            count += 1
    return count


