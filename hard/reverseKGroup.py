# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0) # dummy node since were making modifications
        dummy.next = head # points to head
        prev = dummy # create a prev var

        while True:
            count = 0 # counter
            curr = prev.next # current
            stack = [] # stack

            while curr and count < k: # append to stack
                stack.append(curr)
                curr = curr.next
                count += 1

            if count < k: # return what we have basically (dummy is our next LL)
                return dummy.next
            
            self.reverse(stack) # reverse operation

            stack[0].next = curr # basically just reattaches the reversed list back to the original
            prev.next = stack[-1] 
            prev = stack[0] 

    def reverse(self, nodes):
        """
        Helper function for reversing a linked list in place
        """
        for i in range(len(nodes) - 1, 0, -1): 
            nodes[i].next = nodes[i-1]
