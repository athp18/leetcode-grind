class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: # edge case: matrix doesnt exist
            return False
        
        m, n = len(matrix), len(matrix[0])
        rows, cols = 0, cols - 1

        while row < m and n >= 0:
            try:
                curr = matrix[row][col] # we initialize at the top right. this is so that we don't avoid a dilemma with starting at the top left (where the target element might be bigger than both the right neighbor and bottom neighbor) or at the bottom right (where it could be smaller than either). the variable here is bigger than all of the elements in its row and smaller than all in its column
                if curr == target: # this means we've seen the target
                    return True
                if curr < target: # current is less than target, so we go down a row (where the variable is larger)
                    row += 1
                else: # current is greater than target, so we go to the left (where the variable is smaller)
                    col -= 1
            except:
                return False
        return False


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # This is the exact same as the code on the top, but we start at the bottom left
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        row, col = rows - 1, 0

        while row >= 0 and col <= cols:
            try:
                curr = matrix[row][col]
                if curr == target:
                    return True
                if curr > target:
                    row -= 1
                else:
                    col += 1
            except:
                return False
        return False
