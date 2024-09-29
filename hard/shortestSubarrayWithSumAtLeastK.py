from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        queue = deque()
        shortest = float('inf')
        
        for i in range(len(nums) + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                shortest = min(shortest, i - queue.popleft())
            
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
            
            queue.append(i)
        return shortest if shortest != float('inf') else -1
