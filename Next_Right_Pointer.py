from collections import deque
from typing import Optional

'''
116. Populating Next Right Pointers in Each Node | Medium
You are given a perfect binary tree where all leaves are on the same level, and every parent
has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
--------------------------------------------------------------------------------------------
Have a queue and insert the nodes at each level from right to left. then within a level we
can populate the next right pointer going in order
'''

class Node:
    def __init__(
            self, val: int = 0,
            left: Optional['Node'] = None,
            right: Optional['Node'] = None,
            next: Optional['Node'] = None
            ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return None
    
    queue = deque([root])

    while queue:
        nextRight = None

        for _ in range(len(queue)):
            cur = queue.popleft()
            cur.next = nextRight
            nextRight = cur
        
            if cur.right:
                queue.append(cur.right)
                queue.append(cur.left) # type: ignore
    
    return root
