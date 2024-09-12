class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # create empty matrix, fill with zeroes
        matrix = [[0] * n for _ in range(n)]
        t, b, l, r = 0, n-1, 0, n-1
        # initialize top, bottom, left, and right pointers.
        num = 1
        # initialize variable to increment

        while t <= b and l <= r: # fill the matrix
            for i in range(l, r+1):
                matrix[t][i] = num
                num += 1
            t += 1

            for i in range(t, b+1):
                matrix[i][r] = num
                num += 1
            
            r -= 1

            if t <= b:
                for i in range(r, l - 1, -1):
                    matrix[b][i] = num
                    num += 1
                b -= 1

            if l <= r:
                for i in range(b, t-1, -1):
                    matrix[i][l] = num
                    num += 1
                l += 1
        return matrix
