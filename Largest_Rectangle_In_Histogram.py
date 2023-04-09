from typing import List


'''
84. Largest Rectangle in Histogram | Hard
Given an array of integers heights representing the histogram's bar height where the width
of each bar is 1, return the area of the largest rectangle in the histogram.
------------------------------------------------------------------------------------------
Bruteforce way would be to expand around each index and figuring out what is the max area 
we can get with this index. We actually don't need to expand previous pillars if the height
of the current pillar is less than the height of the previous pillar. Here we can use a
stack to keep track of the heights of the pillars, if heights[i] > stack[-1][1] then we pop
the last element and calculate the max area we can get by using that pillar
    area = pillar height (from stack [-1]) * (current index - start of this height)
We are storing the start of a certain pillar height and the pillar height in stack.
'''


def largestRectangleArea(heights: List[int]) -> int:
    area = 0
    stack = []

    for i, h in enumerate(heights):
        start = i

        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            area = max(area, height * (i - idx))
            start = idx

        
        stack.append((start, h))
    
    for start, h in enumerate(stack):
        area = max(area, h * (len(heights) - start))
    
    return area
