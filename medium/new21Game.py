class Solution:
    @lru_cache(maxsize=None)
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k + maxPts <= n:
            return 1.0 
        elif k > n:
            return 0.0
        
        window = 0
        for i in range(k, k+maxPts):
            window += 1 if i <= n else 0

        dp = {}
        for i in range(k-1, -1, -1):
            dp[i] = window / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)
            window += dp[i] - remove

        return dp[0]
