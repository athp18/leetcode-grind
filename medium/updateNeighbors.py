class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        dist = []
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist.append((i, j))
                else:
                    mat[i][j] = '#'
        
        for r, c in dist:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dx, c + dy
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == '#':
                    mat[nr][nc] = mat[r][c] + 1
                    dist.append((nr, nc))
                    
        return mat # mashallah i finished it
