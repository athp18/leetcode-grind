class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        seen = [[False] * cols for _ in range(rows)]
        res = []

        def dfs(row, col, direction):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or seen[row][col]
            ):
                return

            res.append(matrix[row][col])
            seen[row][col] = True

            if direction == 0:  # move right
                dfs(row, col + 1, 0)
                dfs(row + 1, col, 1)
            elif direction == 1:  # move down
                dfs(row + 1, col, 1)
                dfs(row, col - 1, 2)
            elif direction == 2:  # move left
                dfs(row, col - 1, 2)
                dfs(row - 1, col, 3)
            else:  # move up
                dfs(row - 1, col, 3)
                dfs(row, col + 1, 0)

        dfs(0, 0, 0)
        return res
