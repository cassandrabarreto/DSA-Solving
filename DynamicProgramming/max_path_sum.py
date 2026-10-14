""" 
    Write a function, max_path_sum, that takes in a grid as an argument. 
    The function should return the maximum sum possible by traveling a path from the top-left
    corner to the bottom-right corner. You may only travel through the grid by moving down or right.

    You can assume that all numbers are non-negative.
"""

def max_path_sum(grid):
    return _max_path_sum_helper(grid, 0, 0, {})

def _max_path_sum_helper(grid, row, col, memo):
    position = (row, col)
    if position in memo:
        return memo[position]
    # we should also have inbounds base case
    if row == len(grid) or col== len(grid[0]):
        return float('-inf')
    # if we get to the goal 
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return grid[row][col]

    down = _max_path_sum_helper(grid, row + 1, col, memo)
    right = _max_path_sum_helper(grid, row, col + 1, memo)

    memo[position] = grid[row][col] + max(right, down)
    return memo[position]