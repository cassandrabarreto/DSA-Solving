""" 
    
Write a function, five_sort, that takes in a list of numbers as an argument. The function should rearrange elements of the list 
    
such that all 5s appear at the end. Your function should perform this operation in-place by mutating the original list. 
The function should return the list.

Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.

Important: Your function needs to mutate the original list in-place and should not return a new list. It will fail the test cases if you do not modify the original input list.

five_sort([5, 0])
# -> [0, 5] 

"""
def five_sort(nums):
    i = 0
    j = len(nums) - 1
    
    while i < j:
        if nums[j] == 5:
            j-= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        else:
            i+= 1
    return nums


