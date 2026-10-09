"""
Write a function that takes in an array of positive integers and a target product. 
The function should return the number of 
subarrays that have a total product strictly less than the target.
"""

def count_subarray_product(nums: list[int], target_product : int) -> int:
    start = 0
    subarray_count = 0
    current_product = 1

    for end in range (0, len(nums)):
        lead = nums[end]
        current_product *= lead

        # constraint violation handling
        while current_product >= target_product and start <= end:
            # trailing
            trailing = nums[start]
            current_product /= trailing
            start += 1
        subarray_count += end - start + 1 
    return subarray_count
