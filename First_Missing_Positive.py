import enum
from typing import List

'''
41. First Missing Positive | Hard
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
--------------------------------------------------------------------------------------
The problem is quiet hard due to the given constraints, so lets build up a solution.
1. No constraints
Without any constraints we just sort the array and have a counter starting at 1 then loop
through the array incrementing counter if element == counter else returning the counter
    O(nlogn) time and O(1) space
2. Have to do it in O(n)
Suppose the array is of size n, then at max the first missing positive will be n + 1th
positive number. [1,2,3,4] => 5. So make a new array of size (n + 1) and iterate through
the original array marking the indices that have appeared, then return the first missing
index in the created array.
    O(n) time and O(n) space
3. Both O(n) time and O(1) space
For this we must first eleminate the -ve and > n + 1 numbers, i.e. mark them as n + 1.
Then iterate through the array negating the index corresponding to array[i] if not already
-ve. Iterate through the array once more to get the first missing +ve
    O(n) time and O(1) space
'''

def firstMissingPositive(nums: List[int]) -> int:
    n = len(nums)
    
    for i, num in enumerate(nums):
        if num <= 0 or num > n + 1:
            nums[i] = n + 1
    
    for num in nums:
        i = abs(num)

        if i > n:
            continue

        if nums[i - 1] > 0:
            nums[i - 1] *= -1
    
    for i, num in enumerate(nums):
        if num > 0:
            return i + 1
    
    return n + 1
