from typing import List


'''
48. Rotate Image | Medium
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
---------------------------------------------------------------------------------------------------
Simpley transpose and then swap the columns of the matrix
'''


def rotate(matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(m):
        left, right = 0, len(matrix[i])

        while left <= right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
