# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr, carry = dummy, 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry
            carry = val // 10
            val %= 10

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # If there's any carry left, create a new node for it
        if carry:
            curr.next = ListNode(carry)

        return dummy.next