""" 
Write a function, island_count, that takes in a grid containing Ws and Ls. 
W represents water and L represents land. The function should return the number of islands on the grid.
An island is a vertically or horizontally connected region of land.
"""

def island_count(grid):
    visited = set()
    count = 0
    for row in range (len(grid)):
        for column in range (len(grid[0])):
            if explore(grid, row, column, visited):
                count += 1 
    return count


def explore(grid, r, c , visited):
    row_inbounds = 0 <= r and r < len(grid)
    column_inbounds = 0 <= c and c < len(grid[0])

    # Base Case
    if not row_inbounds or not column_inbounds:
        return False
    
    # Base Case. If we dont find land
    if grid[r][c] == "W":
        return False
    
    position = (r,c)

    # Base Case
    if position in visited:
        return False
    
    visited.add(position)

    # Move down
    explore(grid, r + 1, c, visited)
    #Move up
    explore(grid, r - 1, c, visited)
    # Move to the right
    explore(grid, r , c + 1 , visited)
    # Move to the left
    explore(grid, r , c - 1 , visited)

    return True
    

    