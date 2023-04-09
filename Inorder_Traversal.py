from collections import deque
from typing import List, Optional


'''
94. Binary Tree Inorder Traversal | Easy
Given the root of a binary tree, return the inorder traversal of its nodes' values.
-----------------------------------------------------------------------------------

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def recursiveInorder(root: Optional[TreeNode]) -> List[int]:
    res = []

    def helper(node: Optional[TreeNode]) -> None:
        if node:
            helper(node.left)
            res.append(node.val)
            helper(node.right)
    
    helper(root)
    return res


def iterativeInorder(root: Optional[TreeNode]) -> List[int]:
    res = []
    cur, stack = root, deque([])

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack.popleft()
        res.append(cur.val)
        cur = cur.right
    
    return res
