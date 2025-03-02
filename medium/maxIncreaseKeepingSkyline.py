class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        assert n == len(grid[0]), "why are you lying to me about the problem constraints"
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]

        total = 0
        for i in range(n):
            for j in range(n):
                allowed = min(row_max[i], col_max[j])
                total += allowed - grid[i][j]
        return total
