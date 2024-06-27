class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val) # append the val to the stack
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        try: 
            return self.minStack[-1]
        except:
            return None
