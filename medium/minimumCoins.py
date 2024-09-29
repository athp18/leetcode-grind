class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0 

        for i in range(n - 1, -1, -1):
            current_cost = prices[i]
            next_purchase = min(n, i + i + 2)
            
            # the minimum cost is the current fruit's price plus the minimum cost of the next required purchase
            dp[i] = current_cost + min(dp[i+1 : next_purchase+1])
        
        return dp[0]
