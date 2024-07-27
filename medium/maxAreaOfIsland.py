from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxx = max(maxx, self.dfs(grid, i, j))
        return maxx
    
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        
        # mark as visited
        grid[i][j] = 0
        
        # initial count
        count = 1
        
        # explore recursively
        count += self.dfs(grid, i + 1, j)  # Down
        count += self.dfs(grid, i - 1, j)  # Up
        count += self.dfs(grid, i, j - 1)  # Left
        count += self.dfs(grid, i, j + 1)  # Right
        
        #return
        return count
