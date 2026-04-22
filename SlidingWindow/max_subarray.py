
""" 
Write a function that takes in a list of numbers and a size k as arguments. 
The function should return the maximum sum of subarrays that contain exactly k elements.
You can assume that k is less than or equal to the length of the input list.
"""

# Naive Solution
def max_subarray_sum_size_k(nums, k):
    max_sum = float('-inf')
    # + 1 because range is exclusive on ther right side
    for i in range(0, len(nums) - k + 1):
        current_sum = sum(nums[i:i + k])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum



# Optimized Solution
def max_subarray_sum_size_k(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    # + 1 because range is exclusive on ther right side
    for i in range(0, len(nums) - k):
        # Substract training element
        current_sum -= nums[i]
        current_sum += nums[i + k]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum
