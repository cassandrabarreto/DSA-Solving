""" 

A knight and a pawn are on a chess board. Can you figure out the minimum number of moves 
required for the knight to travel to the same position of the pawn? 
On a single move, the knight can move in an "L" shape; two spaces in any direction, 
then one space in a perpendicular direction. This means that on a single move, a knight 
has eight possible positions it can move to.

Write a function, knight_attack, that takes in 5 arguments:

    n, kr, kc, pr, pc

    n = the length of the chess board
    kr = the starting row of the knight
    kc = the starting column of the knight
    pr = the row of the pawn
    pc = the column of the pawn

The function should return a number representing the minimum number of moves 
required for the knight to land ontop of the pawn. The knight cannot move out-of-bounds of the board. 
You can assume that rows and columns are 0-indexed. 
This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7. 
If it is not possible for the knight to attack the pawn, then return None.    

"""
from collections import deque 
def knight_attack(n, kr, kc, pr, pc):
    visited = set((kr, kc))
    moves = 0
    queue = deque([kr,kc, moves])

    while queue:
        row, column, moves = queue.popleft()
        if (row, column) == (pr, pc):
            return moves
        neighbours = get_knight_moves(n, row, column)

        for neighbour in neighbours:
            neighbour_row , neighbour_col = neighbour

            if neighbour not in visited:
                queue.append((neighbour_row, neighbour_col, moves + 1))
    return None

def get_knight_moves(board_lenght, row, column):
    positions = [
        (row + 2, column + 1 ),
        (row - 2, column + 1),
        (row + 2, column - 1),
        (row - 2, column - 1 ),
        (row + 1, column + 2 ),
        (row - 1, column + 2 ),
        (row + 1, column - 2 ),
        (row - 1, column - 2 ),
    ]

    inbound_positions = []

    for position in positions:
        new_row, new_col = position
        if 0 <= new_row < board_lenght and 0 <= new_col < board_lenght:
            inbound_positions.append(position)
    return inbound_positions


