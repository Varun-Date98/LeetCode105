from collections import deque
from typing import Optional
import math


'''
98. Validate Binary Search Tree | Medium
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
    1. The left subtree of a node contains only nodes with keys less than the node's key.
    2. The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.
---------------------------------------------------------------------------------------------

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def helper(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True
        
        if not (low <= node.val <= high):
            return False
        
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    
    return helper(root, -math.inf, math.inf)


def isValidBST_iterative(root: Optional[TreeNode]) -> bool:
    stack = [(root, -math.inf, math.inf)]

    while stack:
        node, low, high = stack.pop()

        if not node:
            continue

        if not (low <= node.val <= high):
            return False
        
        stack.append((node.left, low, node.val))
        stack.append((node.right, node.val, high))
    
    return True


def isValidBST_extraspace(root: Optional[TreeNode]) -> bool:
    values = []
    cur, stack = root, deque([])

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack.popleft()
        values.append(cur.val)
        cur = cur.right
    
    for i in range(1, len(values)):
        if values[i - 1] > values[i]:
            return False
    
    return True
