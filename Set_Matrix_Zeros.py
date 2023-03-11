from typing import List


'''
73. Set Matrix Zeroes | Medium
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
-----------------------------------------------------------------------------------------------
Can be done trivially with O(n) space by keeping track of the rows and columns that need to be
marked a zeros. To do it without taking any extra space, use the first row and column to keep
track of the row and column that need to be makrd as zeros.
'''


def setZeros(matrix: List[List[int]]) -> None:
    rows, cols = set(), set()
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    
    for r in range(m):
        for c in cols:
            matrix[r][c] = 0
    
    for r in rows:
        for c in range(n):
            matrix[r][c] = 0


def setZerosEff(matrix: List[List[int]]) -> None:
    firstRowZeros = False
    m, n = len(matrix), len(matrix[0])

    for j in range(n):
        if matrix[0][j] == 0:
            firstRowZeros = True
        
        for i in range(1, m):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    
    # Changing all the elements except first row and column
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # If first column is zeros then matrix[0][0] == 0
    if matrix[0][0] == 0:
        for i in range(m):
            matrix[i][0] = 0
    
    # Setting first row as zeros
    if firstRowZeros:
        for j in range(n):
            matrix[0][j] = 0
