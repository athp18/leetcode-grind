# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 1
        last = head

        while last.next:
            last = last.next
            length += 1
        
        k %= length
        if k == 0:
            return head
        
        curr = head # set current variable to traverse
        for i in range(length -k - 1):
            curr = curr.next # traverse the LL
        new = curr.next # new head
        curr.next = None # Break teh connection
        last.next = head # Recreate the linked list. This line essentially reconnects the sliced portion back to the original

        return new

