from collections import deque

class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = deque()
        self.match_count = 0

    def consec(self, num: int) -> bool:
        if len(self.stream) == self.k:
            old = self.stream.popleft()
            if old == self.value:
                self.match_count -= 1

        self.stream.append(num)

        if num == self.value:
            self.match_count += 1

        return len(self.stream) == self.k and self.match_count == self.k
