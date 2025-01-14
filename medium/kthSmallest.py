class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]

        def numLessOrEqual(mid):
            count = 0
            j = n-1
            i = 0

            while i < n and j >= 0:
                if matrix[i][j] <= mid:
                    count += (j + 1)
                    i += 1
                else:
                    j -= 1
            return count
        
        while left < right:
            mid = left + (right - left) // 2
            count = numLessOrEqual(mid)

            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
