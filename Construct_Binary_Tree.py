from collections import defaultdict
from operator import index
from typing import List, Optional


'''
105. Construct Binary Tree from Preorder and Inorder Traversal | Medium
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary
tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
---------------------------------------------------------------------------------------------------

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    Idx = 0
    valToIndex = defaultdict(int)

    def helper(left: int, right: int) -> Optional[TreeNode]:
        nonlocal Idx

        if left > right:
            return
        
        val = preorder[Idx]
        inoredrIdx = valToIndex[val]
        node = TreeNode(val)
        node.left = helper(left, inoredrIdx - 1)
        node.right = helper(inoredrIdx + 1, right)

        return node

    for i, n in enumerate(inorder):
        valToIndex[n] = i
    
    return helper(0, len(inorder) - 1)
