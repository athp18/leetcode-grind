class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1  # First ugly number is 1
        
        # Pointers for multiplying with 2, 3, and 5
        p2 = p3 = p5 = 0
        
        # Generate ugly numbers
        for i in range(1, n):
            nextugly = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            dp[i] = nextugly
            
            if nextugly == dp[p2] * 2:
                p2 += 1
            if nextugly == dp[p3] * 3:
                p3 += 1
            if nextugly == dp[p5] * 5:
                p5 += 1
                
        return dp[n-1]
