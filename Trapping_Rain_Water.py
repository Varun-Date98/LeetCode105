from typing import List

'''
42. Trapping Rain Water | Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
----------------------------------------------------------------------------------------------
In order to calculate the total amount of trapped rain water, we must calculate the amount of
water trapped at every index, then sum up to get the total trapped water. Height of water
column trapped at index i is given by:
water[i] = min(max(pillar heights 0 to i - 1), max(pillar heights i + 1 to n)) - pillar height at i
Brute force approach would involve at each index getting the max left and right pillars and
then calculating the total trapped water. This will lead to an O(n^2) algorithm.
If we iterate through the array storing the left max pillar for each index in an array
then go in reverse while keeping track of right max and calculating the water height, we can
complete this in O(n) time and O(n) space.
'''


def trap(heights: List[int]) -> int:
    leftMax, rightMax = 0, 0
    pillars = [0] * len(heights)

    for i, height in enumerate(heights):
        pillars[i] = leftMax

        if height > leftMax:
            leftMax = height
    
    for i in range(len(heights) - 1, -1, -1):
        pillars[i] = max(0, min(pillars[i], rightMax) - heights[i])

        if heights[i] > rightMax:
            rightMax = heights[i]
    
    return sum(pillars)
