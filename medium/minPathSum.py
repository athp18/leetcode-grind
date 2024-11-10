class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]

        dp[m-1][n-1] = grid[m-1][n-1]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue # this is our base case
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j+1])
                if i + 1 < m:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i+1][j])
        return dp[0][0]
