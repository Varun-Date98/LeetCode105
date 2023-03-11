from collections import defaultdict
from typing import List


"""
75. Sort Colors | Medium
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects
of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
---------------------------------------------------------------------------------------------------
The problem can be solved easily inplace using any inplace sorting technique. Here I go for counting
sort which accomplishes this in O(n) time and O(n) space. To answer a follow up question can you do
it in O(n) time and O(1) space, we need to be familiar with the Dutch Partition Problem.
Here our pointer to the numbers will be lastWhite (this holds the index of the lase white color),
the array is sorted when lastWhite <= lastBlue. So check each element, if color is red, swap with 
lastRed, move lastRed and lastWhite (swapping with lastRed give us red color). If color is white
move lastWhite. If color is Blue swap with lastBlue decrement lastBlue (In an unsorted array swapping 
with lastBlue can give red and white colors as well so we need to check the current index again, hence
not moving lastWhite)
"""


def sortColors(nums: List[int]) -> None:
    # Inplace using counting sort O(n) time and O(n) space
    i = 0
    counts = defaultdict(int)

    for num in nums:
        counts[num] += 1
    
    for num in range(3):
        count = counts[num]

        while count:
            nums[i] = num
            count -= 1
            i += 1


def dutchPartitionProblem(nums: List[int]) -> None:
    # Red: 0, White: 1, Blue: 2
    lastRed, lastWhite, lastBule = 0, 0, len(nums) - 1

    while lastWhite <= lastBule:
        # color at lastWhite is red
        if nums[lastWhite] == 0:
            nums[lastRed], nums[lastWhite] = nums[lastWhite], nums[lastRed]
            lastRed += 1
            lastWhite += 1
        # color at lastWhite is white
        elif nums[lastWhite] == 1:
            lastWhite += 1
        # color at lastWhite is blue
        else:
            nums[lastWhite], nums[lastBule] = nums[lastBule], nums[lastWhite]
            lastBule -= 1
