from typing import List


'''
78. Subsets | Medium
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
--------------------------------------------------------------------------------------------
To get the power set we have two choices for each element, include it in the current set or
not to include it. By not including every element we get the null set [] and by selecting
every element we get the original set, by individually selecting and ignoring the elements
we will get the power set.
'''


def subsets(nums: List[int]) -> List[int]:
    res = []

    def recursion(i: int, cur: List[int]) -> None:
        if i >= len(nums):
            res.append(cur)
            return
        
        recursion(i + 1, cur)               #Not including the current element
        recursion(i + 1, cur + [nums[i]])   #Including the current element
    
    recursion(0, [])
    return res
