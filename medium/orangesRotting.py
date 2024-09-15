from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        
        fresh_oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # Directions for adjacent cells (up, down, left, right)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Variable to keep track of time elapsed
        time_elapsed = 0

        while queue:
            r, c, time = queue.popleft()
            time_elapsed = max(time_elapsed, time)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr, nc, time + 1))
        if fresh_oranges > 0:
            return -1
        else:
            return time_elapsed
