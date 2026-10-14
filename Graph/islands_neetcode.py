
from typing import List

""" 
    
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
You may assume water is surrounding the grid (i.e., all the edges are water).

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        visited = set()
        for row in range (len(grid)):
            for column in range (len(grid[0])):
                if self.explore(grid, row, column, visited):
                    counter += 1
        return counter

    def explore(self, grid, row, column, visited):
        position = (row, column)

        if position in visited:
            return False
        # We need base cases
        # check if position's row and column are inbounds
        row_inbounds = 0 <= row and row < len(grid)
        col_inbounds = 0 <= column and column < len(grid[0])

        if not row_inbounds or not col_inbounds:
            return False
        
        # Check if we are hitting Water, we need to also to stop looking
        if grid[row][column] ==  "0":
            return False

        # Recursive Step
        # if we did not hit any base case, then this node is land. lets add it to visited
        visited.add(position)

        # we need to move up down right and left
        self.explore(grid, row + 1, column, visited)
        self.explore(grid, row - 1, column, visited)
        self.explore(grid, row, column + 1, visited)
        self.explore(grid, row, column - 1, visited)

        return True