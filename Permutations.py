from typing import List, Set

'''
46. Permutations | Medium
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
-----------------------------------------------------------------------------------------------------------------------

'''


def permutations(nums: List[int]) -> List[List[int]]:
    res = []

    def backtracking(curSet: Set[int], curPerm: List[int]):
        if not curSet:
            res.append(curPerm[:])
            return
        
        for num in list(curSet):
            curSet.remove(num)
            backtracking(curSet, curPerm + [num])
            curSet.add(num)
    
    backtracking(set(nums), [])
    return res
