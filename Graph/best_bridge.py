""" 
Write a function, best_bridge, that takes in a grid as an argument.
The grid contains water (W) and land (L). There are exactly two
islands in the grid. An island is a vertically or horizontally 
connected region of land. Return the minimum length bridge needed 
to connect the two islands. A bridge does not need to form a straight line.
"""
from collections import deque

def best_bridge(grid: list[list[str]]) -> int:
    main_island = None
    for row in range (len(grid)):
        for column in range(len(grid[0])):
            potential_island = traverse_island(grid, row, column, set())

            if len(potential_island) > 0:
                main_island = potential_island
                
    # Mark island as visited        
    visited = set(main_island)
    queue = deque([])
    for position in main_island:
        r , c = position
        queue.append((r,c,0))

    while queue:
        row, col , distance = queue.popleft()

        if grid[row][col] == "L" and (row,col) not in main_island:
            return distance - 1

        neighbours = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1)
        ]

        for (neighbour_row, neighbour_col) in neighbours:
            neighbour_position = (neighbour_row, neighbour_col)
            if is_inbounds(grid, neighbour_row, neighbour_col) and neighbour_position not in visited:
                visited.add(neighbour_position)
                queue.append((neighbour_row, neighbour_col, distance + 1))


def is_inbounds(grid: list[list[str]], r: int, c: int) -> bool:
    row_inbouds = 0 <= r and r < len(grid)
    col_inbouds = 0 <= c and c < len(grid[0])
    return row_inbouds and col_inbouds

def traverse_island(grid: list[list[str]], r: int, c: int, visited: set) -> set:
    if not is_inbounds(grid, r, c) or grid[r][c] == "W":
        return visited
    
    position = (r, c)

    if position in visited:
        return visited
    
    visited.add(position)

    traverse_island(grid, r -1, c, visited)
    traverse_island(grid, r+1, c, visited)
    traverse_island(grid, r, c+1, visited)
    traverse_island(grid, r, c-1, visited)

    return visited
