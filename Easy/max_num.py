

def max_num(nums):
    max = float('-inf')

    for num in nums:
        if num > max:
            max = num
    return max_num