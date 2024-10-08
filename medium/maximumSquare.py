class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        r, c = len(matrix), len(matrix[0])

        dp = [[0] * c for _ in range(r)]
        MAX = 0

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    MAX = max(MAX, dp[i][j])
        return MAX ** 2
