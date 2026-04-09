""" 
Write a function, minimum_island, that takes in a grid containing Ws and Ls.
W represents water and L represents land. The function should return the size of 
the smallest island. An island is a vertically or horizontally connected region of land.
You may assume that the grid contains at least one island.

"""

def minimum_island(grid):
    visited = set()
    island_sizes = []
    for row in range(len(grid)):
        for column in range (len(grid[0])):
            count = explore(grid, row, column, visited)
            if count > 0:
                island_sizes.append(count)
    return min(island_sizes, default=0)


def explore(grid, r, c , visited):
    row_inbound = 0 <= r and r < len(grid)
    column_inbound = 0 <= c and c < len(grid[0])
    
    # Base Case
    if not row_inbound or not column_inbound:
        return 0
    # If its water then we also dont care about exploring
    if grid[r][c] == "W":
        return 0

    position = (r,c)
    
    # If we have already visited it
    if position in visited:
        return 0

    visited.add(position)
    size = 1
    size += explore(grid, r - 1, c , visited)
    size += explore(grid, r + 1, c, visited)
    size += explore(grid, r, c - 1 , visited)
    size += explore(grid, r, c + 1, visited)
    return size