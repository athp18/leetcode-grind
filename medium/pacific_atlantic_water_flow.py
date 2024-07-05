class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable):
            reachable.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable)
        
        # Start DFS from all cells in the first row and the first column
        for i in range(rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, cols - 1, atlantic_reachable)
        
        for j in range(cols):
            dfs(0, j, pacific_reachable)
            dfs(rows - 1, j, atlantic_reachable)
        
        # Find intersection of pacific_reachable and atlantic_reachable
        result = list(pacific_reachable.intersection(atlantic_reachable))
        
        return result
