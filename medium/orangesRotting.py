class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = fresh = minutes = 0
        queue = []
        
        #
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == 1:
                    fresh += 1
                elif cell == 2:
                    queue.append(i * n + j)
                    rotten += 1
        
        # Early exit checks
        if fresh == 0: 
            return 0
        if rotten == 0: 
            return -1
        
        #start index for current minute's batch
        start = 0
        
        #process oranges level by level without deque
        while start < len(queue):
            size = len(queue) - start
            
            for _ in range(size):
                pos = queue[start]
                r, c = divmod(pos, n)
                start += 1
                
                for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                    if (0 <= nr < m and 0 <= nc < n and 
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append(nr * n + nc)
                        fresh -= 1
            
            minutes += 1
            
            if fresh == 0:
                return minutes
                
        return -1
