from typing import List


'''
53. Maximum Subarray | Medium
Given an integer array nums, find the subarray with the largest sum, and return its sum.
----------------------------------------------------------------------------------------
Can be done in multiple ways, a n^2 approach has us calculate the prefix sum of the given array
and then we can iterate over all possible sub arrays and get their sum in O(1) from the prefix
sum. To accomplish this in O(n) we must understand that if a subarray sum becomes negative,
it will not contribute to max subarray sum for any of the subsequent subarrays. So whenever
the current subarray sum becomes -ve we ignore it and start over.
'''


def maxSubArrayQuadratic(nums: List[int]) -> int:
    prefix, res = [0], nums[0]

    for num in nums:
        prefix.append(prefix[-1] + num)
    
    for i in range(1, len(nums)):
        for j in range(i):
            res = max(res, prefix[i] - prefix[j])
    
    return res


def maxSubArray(nums: List[int]) -> int:
    cur, res = 0, nums[0]

    for num in nums:
        cur += num
        res = max(res, cur)

        if cur < 0:
            cur = 0
    
    return res