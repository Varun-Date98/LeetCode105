from typing import Optional

"""
2. Add Two Numbers | Medium
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

--------------------------------------------------------------------------------------------

Easiest way would be to initialise a dummy node and then add the numbers like in mergesort
A better implementation with just one while loop is shown here
"""


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    ptr1, ptr2, ptr3, carry = l1, l2, dummy, 0

    while ptr1 or ptr2 or carry:
        a = ptr1.val if ptr1 else 0
        b = ptr2.val if ptr2 else 0
        digit, carry = (a + b + carry) % 10, (a + b + carry) // 10

        ptr3.next = ListNode(digit)
        ptr3 = ptr3.next
        ptr1 = ptr1.next if ptr1 else None
        ptr2 = ptr2.next if ptr2 else None

    return dummy.next
