import heapq
from typing import List, Optional

'''
23. Merge k Sorted Lists | Hard
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
----------------------------------------------------------------------------------------------

'''


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Wrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    dummy = cur = ListNode()

    for head in lists:
        if head:
            heapq.heappush(heap, head)
    
    while heap:
        node = heapq.heappop(heap).node
        cur.next = node
        cur = cur.next

        if node.next:
            heapq.heappush(heap, node.next)
    
    return dummy.next
