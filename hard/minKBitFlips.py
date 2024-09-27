from collections import deque


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        queue = deque()
        res = 0

        for i in range(len(nums)):
            # heres why we want a queue
            while queue and i > queue[0] + k - 1:
                queue.popleft()

            if (nums[i] + len(queue)) % 2 == 0:
                if i + k > len(nums):
                    # we dont have k elems remaining
                    return -1
                res += 1
                queue.append(i)
        return res
