
""" 
Write a function that takes in a list and a target sum. 
The function should return the start and end indices (inclusive) of a 
subarray that sums to the target.
You can assume that the elements of the list are nonnegative.
You can assume that there is exactly one subarray that sums to the target    
"""

def find_subarray_sum(nums: list, target_sum: int) -> int:
    start = 0
    window_sum = 0

    for end in range (0,len(nums)):
        # Add up element
        window_sum += nums[end]

        # While the window is bigger than the target, make it smaller
        while window_sum > target_sum:
            window_sum -= nums[start]
            # Shift start to the right to shrink the window.
            start += 1
        if window_sum == target_sum:
            return (start, end)






