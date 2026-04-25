

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



def max_subarray_sum_size_k(nums, k):
    # Process first window 
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]

        max_sum = max(current_sum, max_sum)
    return max_sum


