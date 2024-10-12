from collections import deque

class MyStack:

    def __init__(self):
        self.main = deque()
        self.helper = deque()

    def push(self, x: int) -> None:
        self.helper.append(x)
        while self.main:
            self.helper.append(self.main.popleft())
        self.main, self.helper = self.helper, self.main

    def pop(self) -> int:
        return self.main.popleft()

    def top(self) -> int:
        return self.main[0]
        
    def empty(self) -> bool:
        return not self.main
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
