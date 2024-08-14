class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        left = [0] * n
        right = [0] * n
        
        MIN = float('inf')
        for i in range(n):
            MIN = min(MIN, prices[i])
            if i > 0:
                left[i] = max(left[i-1], prices[i] - MIN)
            else:
                left[i] = 0

        MAX = float('-inf')
        for i in range(n-1, -1, -1):
            MAX = max(MAX, prices[i])
            if i < n-1:
                right[i] = max(right[i+1], MAX - prices[i])
            else:
                right[i] = 0

        MAX = 0
        for i in range(n):
            MAX = max(MAX, left[i] + right[i])
        
        return MAX
