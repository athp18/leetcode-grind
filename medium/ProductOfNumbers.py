from collections import deque

class ProductOfNumbers:
    def __init__(self):
        self.stream = deque([1])
        self.curr = 1
        
    def add(self, num: int) -> None:
        if num == 0:
            self.stream.clear()
            self.stream.append(1)
            self.curr = 1
        else:
            self.curr *= num
            self.stream.append(self.curr)

    def getProduct(self, k: int) -> int:
        if k > len(self.stream) - 1:
            return 0
        if k == len(self.stream) - 1:
            return self.curr
        return self.curr // self.stream[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
