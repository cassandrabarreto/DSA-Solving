""" 
Write a function, pair_sum, that takes in a list and a target sum as arguments. 
The function should return a tuple containing a pair of indices whose elements sum to the given target. 
The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

"""

def pair_sum(nums, target):
    nums_dict = {}
    
    for index, element in enumerate(nums):
        complement = target - element
    
        if complement in nums_dict:
            return (nums_dict[complement], index)
        else:
            nums_dict[element] = index
        


print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)
print(pair_sum([9, 9], 18) )