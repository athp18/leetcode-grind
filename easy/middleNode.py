# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        mid = length // 2
        curr = head

        for i in range(mid):
            curr = curr.next
        return curr
