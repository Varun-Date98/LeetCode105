from typing import List, Optional

'''
15. 3Sum | Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
---------------------------------------------------------------------------------
Use same approach as two sum, fix the first number then find the second and third
numbers using left and right pointers. Keep in maind if nums[i] == nums[i + 1],
i.e. there are duplicates, just continue the loop instead.
'''


def threeSum(nums: List[int]) -> Optional[List[int]]:
    res = []
    nums.sort()

    for i, num in enumerate(nums):
        target = -num
        left, right = i + 1, len(nums) - 1

        # Optimazation as no three +ve numbesr can sum up to 0
        if num > 0:
            break

        if i > 0 and nums[i - 1] == nums[i]:
            continue

        while left < right:
            cur = nums[left] + nums[right]

            if cur > target:
                right -= 1
            elif cur < target:
                left += 1
            else:
                triplet = [num, nums[left], nums[right]]
                res.append(triplet)

                while left < right and nums[left] == triplet[1]:
                    left += 1
                
                while left < right and nums[right] == triplet[2]:
                    right -= 1
    
    return res
