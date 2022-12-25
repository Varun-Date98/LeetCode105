from typing import List

'''
33. Search in Rotated Sorted Array | Medium
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
(1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated
at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of
target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
-----------------------------------------------------------------------------------------------
Have to use binary search due to the constraints of the problem.
Firstly perform a binary search to find possible rotation index k
This can be done by comparing the mid and right
'''

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    # Perform binary search to find the index of min, thus finding the rotation index
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    k = left

    # Once we have the rotation index k we can calcualte actual indices in the array
    # i` = i + k => i = i` - k

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        realMid = (mid + k) % len(nums)

        if nums[realMid] == target:
            return realMid
        elif nums[realMid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1
