
""" 
    Write a function, closest_carrot, that takes in a grid, a starting row, 
    and a starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right, but cannot pass through walls (X).
    If there is no possible path to a carrot, then return -1.

"""
import typing
from collections import deque
def closest_carrot(grid: list[list[str]], starting_row: int, starting_col: int)  -> int:
    visited = set([(starting_row, starting_col)])
    # Initialize position as zero
    queue = deque([(starting_row, starting_col, 0)])

    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == "C":
            return distance
        
        deltas = [(1,0), (-1, 0), (0,1), (0,-1)]
        for delta in deltas:
            delta_row , delta_column = delta
            neighbour_row = row + delta_row
            neighbour_column = col + delta_column
            row_inbounds = 0<= neighbour_row < len(grid)
            column_inbounds = 0<= neighbour_column < len(grid[0])
            position = (neighbour_row, neighbour_column)

            if row_inbounds and column_inbounds and grid[neighbour_row][neighbour_column] != 'X' and position not in visited:
                queue.append((neighbour_row, neighbour_column, distance + 1))
                visited.add(position)
    return -1 

def closest_carrot_easier_solution(grid: list[list[str]], starting_row: int, starting_col: int)  -> int:
    
    # Create queue
    queue = deque([(starting_row, starting_col, 0)])
    visited = set([starting_row, starting_col])

    while queue:
        row, column , distance = queue.popleft()

        if grid[row][column] == "C":
            return distance
        # r + 1, c
        # r -1 , c
        # r , c + 1
        # r , c - 1
        neighbours = [
            (row + 1, column),
            (row - 1, column),
            (row, column + 1),
            (row, column + -1)
        ]

        for (neighbor_row,  neighbor_col) in neighbours:
            row_inbounds = 0 <= neighbor_row and neighbor_row < len(grid)
            column_inbounds = 0 <= neighbor_col and neighbor_col < len(grid[0])
            position = (neighbor_row, neighbor_col)

            if row_inbounds and column_inbounds and grid[neighbor_row][neighbor_col] != 'X' and position not in visited:
                queue.append((neighbor_row, neighbor_col, distance + 1))
                visited.add(position)
    return -1


