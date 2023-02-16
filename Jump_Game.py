from typing import List

'''
55. Jump Game | Medium
You are given an integer array nums. You are initially positioned at the array's first index
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
---------------------------------------------------------------------------------------------
'''


def jumpGame(nums: List[int]) -> bool:
    n = len(nums)
    horizon, cur = nums[0], 0

    while cur <= min(n - 1, horizon):
        horizon = max(horizon, cur + nums[cur])
        cur += 1
    
    return horizon >= n