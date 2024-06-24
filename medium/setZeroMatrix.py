class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        col_set = set()
        row_set = set()
        
        # First pass to find all the zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col_set.add(j)
                    row_set.add(i)
        
        # Zero out the rows
        for i in row_set:
            for j in range(n):
                matrix[i][j] = 0
        
        # Zero out the columns
        for j in col_set:
            for i in range(m):
                matrix[i][j] = 0
