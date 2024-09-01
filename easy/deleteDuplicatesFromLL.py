# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
The trick here is that the linked list is sorted. So the duplicates will be right next to each other.

This means we can avoid use of e.g. a set. If the question were such that "delete duplicates from an unsorted linked list," we might do something like this:

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        seen = set()
        seen.add(curr.val)
        
        while curr and curr.next:
            if curr.next.val in seen:
                curr.next = curr.next.next
            else:
                seen.add(curr.next.val)
                curr = curr.next
                
        return head
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
