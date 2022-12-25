from typing import List

'''
26. Remove Duplicates from Sorted Array | Easy
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
unique element appears only once. The relative order of the elements should be kept the same. Since it is
impossible to change the length of the array in some languages, you must instead have the result be placed
in the first part of the array nums. More formally, if there are k elements after removing the duplicates
then the first k elements of nums should hold the final result. It does not matter what you leave beyond
the first k elements. Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
-----------------------------------------------------------------------------------------------------------

'''


def removeDuplicates(nums: List[int]) -> int:
    Idx, i = 0, 0

    while i < len(nums):
        num = nums[Idx]

        while i < len(nums) and nums[i] == num:
            i += 1
        
        if i < len(nums):
            nums[Idx + 1], nums[i] = nums[i], nums[Idx + 1]
            i += 1
        else:
            break

        Idx += 1
    
    return Idx + 1
