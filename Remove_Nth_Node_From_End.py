from tkinter.messagebox import NO
from typing import Optional

'''
19. Remove Nth Node From End of List | Medium
Given the head of a linked list, remove the nth node from the end of the list and return its head.
--------------------------------------------------------------------------------------------------
Can use one pass to get the length then in the second pass remove the nth node from end
We can also use fast and slow pointers, after fast has moved n nodes, increment both till fast reaches
the end and remove slow.next
'''


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> Optional[ListNode]:
    slow = fast = head

    if head is None:
        return
    
    for _ in range(n):
        # Had to add if conditions to avoid type errors from pylance
        if fast is not None:
            fast = fast.next
    
    # If If we have already reached the end, i.e. we need to remove head
    if not fast:
        return head.next
    
    while fast.next:
        if fast is not None and slow is not None:
            slow, fast = slow.next, fast.next
    
    if slow is not None and slow.next is not None:
        slow.next = slow.next.next

    return head
