from typing import List


'''
118. Pascal's Triangle | Easy
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
-------------------------------------------------------------------------------------------

'''


def generate(numRows: int) -> List[List[int]]:
    triangle = [[1]]

    for i in range(1, numRows):
        x = [0] + triangle[i - 1]
        y = triangle[i - 1] + [0]
        triangle.append([a + b for a, b in zip(x, y)])
    
    return triangle
