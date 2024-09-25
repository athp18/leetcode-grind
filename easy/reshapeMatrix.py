class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        t = r * c
        if (m == r and n == c) or (t != m * n): ## check for possibility
            return mat
        
        res = [[0 for _ in range(c)] for _ in range(r)] ## initialize result array

        i = 0
        for j in range(m):
            for k in range(n):
                res[i//c][i%c] = mat[j][k] # 
                i += 1
        return res
