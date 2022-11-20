from typing import List

'''
1. Two Sum | Difficulty: Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

-------------------------------------------------------------------------------------------------------------------------

Without any constraints this problem is trivial and can be easily sloved in many ways
    1. Two for loops calculating every possible two sum and comparing it with target
    2. Using hash map to store seen numbers and checking if target - num was seen

If interviewer asks what happens if I give you a sorted array, how better can you solve this then use the two pointer approach
'''

def twoSumTwoPointers(array: List[int], target: int) -> List[int]:
    array.sort()
    left, right = 0, len(array) - 1

    while left < right:
        currrentSum = array[left] + array[right]

        if currrentSum < target:
            left += 1
        elif currrentSum > target:
            right -= 1
        else:
            return [left, right]
    
    # If no elements found that sum up to target
    return [-1, -1]

def twoSumSet(array: List[int], target: int) -> List[int]:
    seen = {}

    for i, num in enumerate(array):
        if target - num in seen:
            return [seen[target - num], i]
        
        seen[num] = i

    # If no elements found that sum up to target
    return [-1, -1]