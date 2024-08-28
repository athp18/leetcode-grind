from collections import deque
# definitely not the most efficient but whatever

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        averages = []
        count = 0

        nums.sort()

        DEQUE = deque(nums)

        while count != n // 2:
            a = DEQUE.popleft()
            b = DEQUE.pop()

            averages.append((a+b) / 2)

            count += 1
        return min(averages)

