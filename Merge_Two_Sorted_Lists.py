from typing import Optional

'''
21. Merge Two Sorted Lists | Easy
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.
----------------------------------------------------------------------
Can start by creating a new list two store the merged list and add
nodes inorder. Recursivelu can be done by returning the correct node.
Can be done iteratively as well with O(1) memory by declaring a dummy node
'''


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def mergeSortedListsIterative(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if None in (list1, list2):
        return list1 or list2
    
    dummy = cur = ListNode()
    ptr1, ptr2 = list1, list2

    while ptr1 and ptr2:
        if ptr1.val < ptr2.val:
            cur.next = ptr1
            ptr1 = ptr1.next
        else:
            cur.next = ptr2
            ptr2 = ptr2.next
        
        cur = cur.next
    
    if ptr1:
        cur.next = ptr1
    else:
        cur.next = ptr2
    
    return dummy.next


def mergeSortedListsRecursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    
    if not list2:
        return list1
    
    if list1.val < list2.val:
        list1.next = mergeSortedListsRecursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeSortedListsRecursive(list1, list2.next)
        return list2
