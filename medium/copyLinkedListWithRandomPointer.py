"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None: None}
        curr = head

        # copy the nodes
        while curr:
            copy = Node(curr.val) # this creates a deep copy
            # similar to how float(val) creates a different float object
            copies[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copies[curr]
            copy.next = copies[curr.next]
            copy.random = copies[curr.random] 
            curr = curr.next

        return copies[head]
