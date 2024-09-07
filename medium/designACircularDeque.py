from collections import deque
# with the collections library
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.appendleft(value)
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.deque) > 0:
            self.deque.popleft()
            return True
        else:
            return False
    def deleteLast(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1
    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        else:
            return -1
    def isEmpty(self) -> bool:
        if len(self.deque) == 0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if len(self.deque) == self.k:
            return True
        else:
            return False

#without the collections library
class MyCircularDeque1:

    def __init__(self, k: int):
        self.k = k
        self.deque = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.k:
            return False  # The deque is full
        
        # Move front index back circularly
        self.front = (self.front - 1) % self.k
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.k:
            return False  # The deque is full
        
        # Insert value at rear index
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False  # The deque is empty
        
        # Move front index forward circularly
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False  # The deque is empty
        
        # Move rear index back circularly
        self.rear = (self.rear - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1  # The deque is empty
        
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.size == 0:
            return -1  # The deque is empty
        
        # Rear index needs adjustment since it points to the next empty slot
        return self.deque[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
