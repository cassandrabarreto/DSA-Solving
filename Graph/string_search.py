
""" 
Write a function, string_search, that takes in a grid of letters and a string as arguments. 
The function should return a boolean indicating whether or not the string can be 
found in the grid as a path by connecting horizontal or vertical positions. 
The path can begin at any position, but you cannot reuse a position more than once in the path.

You can assume that all letters are lowercase and alphabetic

"""

def string_search(grid, s):
    for row in range (len(grid)):
        for column in range (len(grid[0])):
            if perform_dfs_search(grid, s, row, column):
                return True
    return False

def perform_dfs_search(grid, string, row, column):
    # Prepare Base Cases

    # First base case represents when the string has been shrinked till nothing is there
    if string == "":
        return True

    row_inbound = 0 <= row and row < len(grid)
    col_inbound = 0 <= column and column < len(grid[0])

    # if not inbounds, return False
    if not row_inbound or not col_inbound:
        return False

    # Look if character is different from string
    current_char = grid[row][column]
    
    if current_char != string[0]:
        return False

    # shrink the string suffix
    string_suffix = string[1:]

    # override current position
    grid[row][column] = "*"

    result = perform_dfs_search(grid, string_suffix, row - 1, column) or \
    perform_dfs_search(grid, string_suffix, row + 1, column) or \
    perform_dfs_search(grid, string_suffix, row, column + 1 ) or \
    perform_dfs_search(grid, string_suffix, row, column - 1 )  \
    
    grid[row][column] = current_char
    return result
    