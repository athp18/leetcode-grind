class Solution: # yeah its O(n3) ... idc
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        
        m, n = len(mat), len(mat[0])
        total = 0
        
        # compute the heights of consecutive 1's for each column
        heights = [[0] * n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if mat[i][j] == 1:
                    heights[i][j] = heights[i-1][j] + 1 if i > 0 else 1
        
        # count the submatrices
        for i in range(m):
            for j in range(n):
                min_height = float('inf')
                for k in range(j, -1, -1):
                    min_height = min(min_height, heights[i][k])
                    total += min_height
        
        return total
