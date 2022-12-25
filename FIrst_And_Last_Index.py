from typing import List

'''
34. Find First and Last Position of Element in Sorted Array | Medium
Given an array of integers nums sorted in non-decreasing order, find the starting and ending
position of a given target value. If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
---------------------------------------------------------------------------------------------
Whenever we see O(log n) time constraints we should think of binary search
Here we have to do two binary searches one for
    1. Index of element <= target
    2. Index of element >= target
Then we just compare that these indices are valid, i.e. withing the array and elements == target
'''


def searchRange(nums: List[int], target: int) -> List[int]:
    # If we get an empty list
    if not nums:
        return [-1, -1]
    
    l, r = bisectLeft(nums, target), bisectRight(nums, target)

    if l == len(nums) or nums[l] != target:
        return [-1, -1]
    
    return [l, r - 1]


def bisectLeft(array: List[int], n: int) -> int:
    """
    Function to return the index of the first element that is less than or
    equal to given target number.
    
    Args:
        array (List[int]): Array of integers
        n (int): Target number

    Returns:
        int: Index of the first element less than or equal to target number
    """

    left, right = 0, len(array)

    while left < right:
        mid = left + (right - left) // 2

        if array[mid] < n:
            left = mid + 1
        else:
            right = mid
    
    return left


def bisectRight(array: List[int], n: int) -> int:
    """
    Function to return the index of the first element that is greater than or
    equal to given target number.
    
    Args:
        array (List[int]): Array of integers
        n (int): Target number

    Returns:
        int: Index of the first element greater than or equal to target number
    """

    left, right = 0, len(array)

    while left < right:
        mid = left + (right - left) // 2

        if array[mid] > n:
            right = mid
        else:
            left = mid + 1
    
    return left
