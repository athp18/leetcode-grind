class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        mins = [min(row) for row in matrix]
        maxs = [max(col) for col in zip(*matrix)] 

        res = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == mins[i] and matrix[i][j] == maxs[j]:
                    res.append(matrix[i][j])
        return res
