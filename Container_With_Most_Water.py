from typing import List

'''
11. Container With Most Water | Medium
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container
such that the container contains the most water. Return the maximum amount of water a container can store.

Notice that you may not slant the container.
------------------------------------------------------------------------------------------------------------------
Brute force approach involves two loops to run over all the pairs of heaghts and the calculate the volume.

If we use two pointers then we can get the maximum area by looping over the heights only once.
'''


def maxVolumeOfWater(heights: List[int]) -> int:
    maxVolume = 0
    left, right = 0, len(heights) - 1

    while left < right:
        width = right - left
        volume = width * min(heights[left], heights[right])
        maxVolume = max(maxVolume, volume)

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    
    return maxVolume
