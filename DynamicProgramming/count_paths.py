""" 
    Write a function, count_paths, that takes in a grid as an argument. 
    In the grid, 'X' represents walls and 'O' represents open spaces. 
    You may only move down or to the right and cannot pass through walls.
    The function should return the number of ways possible to travel from the 
    top-left corner of the grid to the bottom-right corner.
"""

def count_paths(grid):
    return _count_paths_helper(grid, 0 , 0 ,{})

def _count_paths_helper(grid, row, column, memo):
    position = (row, column)

    # Base Cases
    if position in memo:
        return memo[position]

    # If its out ouf of bands or hits invalid path
    if row == len(grid) or column == len(grid[0]) or grid[row][column] == "X":
        return 0

    if row == len(grid) - 1 and column == len(grid[0]) - 1:
        return 1

    # We can only move down or right
    memo[position] = _count_paths_helper(grid, row + 1, column, memo) + _count_paths_helper(grid, row, column + 1, memo)
    return memo[position]
    