
""" 
    
Write a function that takes in an list and a target sum. 
The function should return the length of the longest subarray that sums to the target.
You can assume that the elements of the list are nonnegative.
If there is no subarray that sums to the target, then return -1.
"""

def longest_subarray_sum(nums: list, target_sum: int) -> int:
    current_sum = 0
    start = 0
    max_lenght = 0

    for end in range (0, len(nums)):
        current_sum += nums[end]

        while current_sum > target_sum:
            # shrink the window
            current_sum -= nums[start]
            start += 1
        # check the lenght of subarray
        lenght = len(nums[start:end+1])
        if current_sum == target_sum:
            # Check if current lenght is bigger than max_lenght
            max_lenght = max(lenght, max_lenght)
    
    return -1 if max_lenght == 0 else  max_lenght











""" 
    
Write a function that takes in an list and a target sum. The
 function should return the length of the longest subarray that sums to the target.
You can assume that the elements of the list are nonnegative.
If there is no subarray that sums to the target, then return -1.
"""

def longest_subarray_sum(nums, target_sum):
    # define start 
    start = 0
    max_lenght = 0
    current_sum = 0

    for end in range (0, len(nums)):
        # add up end 
        current_sum += nums[end]

        while current_sum > target_sum:
            # shrink list
            current_sum -= nums[start]
            start += 1
        if current_sum == target_sum:
            current_lenght = len(nums[start:end + 1])
            max_lenght = max(max_lenght, current_lenght)
    return max_lenght if max_lenght > 0 else -1


    