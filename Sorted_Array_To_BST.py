from typing import List, Optional

'''
108. Convert Sorted Array to Binary Search Tree | Easy
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
---------------------------------------------------------------------------------------------------------------------------------
Hight balanced tree can be constructed by picking the middle element of the array as the root node at each point.
'''

class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def constructor(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return 
        
        if left == right:
            return TreeNode(nums[left])
        
        mid = left + (right - left) // 2
        node = TreeNode(nums[mid])
        node.left = constructor(left, mid - 1)
        node.right = constructor(mid + 1, right)
        return node
    
    return constructor(0, len(nums) - 1)
