class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class BrowserHistory:
    def __init__(self, homepage: str):
        # Initialize with homepage as first node
        self.current = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        # Create new node with link to current node as prev
        new_node = ListNode(url, self.current, None)
        # Link current node to new node
        self.current.next = new_node
        # Move current pointer to new node
        self.current = new_node
        
    def back(self, steps: int) -> str:
        # Move back through history up to the number of steps
        # or until we hit the beginning
        temp = self.current
        count = 0
        
        # Move backwards using prev pointers
        while temp.prev and count < steps:
            temp = temp.prev
            count += 1
            
        self.current = temp
        return self.current.val
        
    def forward(self, steps: int) -> str:
        # Move forward through history up to the number of steps
        # or until we hit the end
        temp = self.current
        count = 0
        
        while temp.next and count < steps:
            temp = temp.next
            count += 1
            
        self.current = temp
        return self.current.val
