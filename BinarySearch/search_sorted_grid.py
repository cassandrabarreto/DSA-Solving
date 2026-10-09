""" 
    
Write a function that takes in a grid of numbers and a target element as input. 
The function should return a boolean indicating whether or not the target is present in the grid. 
Each row of the grid is sorted in increasing order. The first element of each row is greater than 
the last element of the previous row.

Your solution should have a time complexity of O(log(m*n)), where m is the 
number of rows and n is the number of columns in the grid.

"""

def find_row(grid, target):
    low = 0
    high = len(grid) - 1

    while low <= high:
        # calculate mid row
        mid = (low + high) // 2
        # compare target with first and last element from the mid row
        if grid[mid][0] <= target <= grid[mid][-1]:
            return mid
        elif target < grid[mid][0]:
            # if the target is less than first element, we need to move to a previous row
            high = mid - 1 
        else:
            low = mid + 1 
    return -1 


def binary_search_row(grid, target, row):
    low = 0 
    high = len(grid[0]) - 1

    while low <= high:
        mid = (low + high) // 2
        if target > grid[row][mid]:
            low = mid + 1
        elif target < grid[row][mid]:
            high = mid - 1
        else:
            return True
    return False
        
 
def search_sorted_grid(grid, target):
    row = find_row(grid, target)
    if row == -1:
        return False
    else:
        return binary_search_row(grid, target, row)