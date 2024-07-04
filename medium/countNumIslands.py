# Now, let's do a DFS solution
# This will have O(n2) time complexity and O(n) space complexity
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        seen = set()
        count = 0
        
        def bfs(r, c):
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            while q:
                row, col = q.pop() # make popleft for bfs lol
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in seen:
                        q.append((nr, nc))
                        seen.add((nr, nc))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in seen:
                    bfs(i, j)
                    count += 1
        return count
