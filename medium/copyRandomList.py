"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# we can do this in either two or three passes
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # pass 1
        if not head:
            return None
        
        # copy the values
        hashmap = {}
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        # copy the pointers
        curr = head
        while curr:
            if curr.next:
                hashmap[curr].next = hashmap[curr.next]
            curr = curr.next
        
        
        curr = head
        while curr:
            if curr.random:
                hashmap[curr].random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]

class Solution1:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # pass 1
        if not head:
            return None
        
        # copy the values
        hashmap = {None: None}
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val) # create a new object
            curr = curr.next # increment
        
        # copy the pointers
        curr = head
        while curr:
            copy = hashmap[curr] # find the copy of the current value
            copy.next = hashmap[curr.next] # set the next pointer. basically: the pointer of our copy is set to the hashmap's copy of curr.next
            copy.random = hashmap[curr.random] # same thing, but set the random pointer
            curr = curr.next # update curr by 1

        return hashmap[head]

