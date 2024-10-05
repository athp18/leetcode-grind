from collections import deque

class MinStack:
    def __init__(self):
        self.stack = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if popped == self.minstack[-1]:
                self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            top_val = self.stack[-1]
            return top_val
        else:
            return -1 

    def getMin(self) -> int:
        if self.minstack:
            min_val = self.minstack[-1]
            return min_val
        else:
            return -1 
