from collections import defaultdict, deque
from typing import List, Optional


'''
102. Binary Tree Level Order Traversal | Medium
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).
---------------------------------------------------------------------------------------

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderTraversal_recursive(root: Optional[TreeNode]) -> List[List[int]]:
    levels = defaultdict(list)

    def helper(node: Optional[TreeNode], depth: int) -> None:
        if not node:
            return
        
        levels[depth].append(node.val)
        helper(node.left, depth + 1)
        helper(node.right, depth + 1)
    
    helper(root, 0)
    return [level for level in levels.values()]


def levelOrderTraversal_iterative(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    level = deque([root])

    while level:
        n = len(level)
        res.append([node.val for node in level if node])

        while n:
            n -= 1
            node = level.popleft()

            if node:
                level.append(node.left)
                level.append(node.right)
    
    res.pop()
    return res
