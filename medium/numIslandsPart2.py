class Solution:
  # dfs approach
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        seen = set()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or (i, j) in seen:
                return
            
            seen.add((i, j))

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    dfs(i, j)
                    count += 1
        return count

from collections import deque

class Solution1: # bfs approach
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        count = 0

        def bfs(r, c):
            queue = deque()
            seen.add((r, c))
            queue.append((r, c))

            while queue:
                r, c = queue.popleft()
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for a, b in dirs:
                    if ((r + a) in range(m) and (c + b) in range(n) and grid[r+a][c+b] == '1' and (r +a, c +b) not in seen):
                        queue.append((r+a, c + b))
                        seen.add((r + a, c + b))
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r,c) not in seen:
                    bfs(r, c)
                    count += 1
        return count

