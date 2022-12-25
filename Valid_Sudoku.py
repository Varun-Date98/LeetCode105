from typing import List

from matplotlib.pyplot import box

'''
36. Valid Sudoku | Medium
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
-------------------------------------------------------------------------------------------------------------------------
Have sets for each row, column and 3 x 3 sub-box, then pass through the grid and check for duplicates.
'''

def validSudoku(board: List[List[str]]) -> bool:
    rows = [set() for row in board]
    cols = [set() for col in board[0]]
    boxes = {(a, b): set() for a in range(3) for b in range(3)}

    for i in range(len(board)):
        for j in range(len(board[0])):
            n = board[i][j]

            if n == '.':
                continue

            if n in rows[i] or n in cols[j] or n in boxes[(i // 3, j // 3)]:
                return False
            
            rows[i].add(n)
            cols[j].add(n)
            boxes[(i // 3, j // 3)].add(n)
    
    return True
