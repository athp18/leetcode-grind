class Solution:
    def solveNQueens(self, n):
        solutions = []
        queens = [-1] * n
        columns = [False] * n
        diagonals1 = [False] * (2 * n - 1)
        diagonals2 = [False] * (2 * n - 1)
        self.backtrack(solutions, queens, n, 0, columns, diagonals1, diagonals2)
        return solutions

    def backtrack(self, solutions, queens, n, row, columns, diagonals1, diagonals2):
        if row == n:
            solutions.append(self.generateBoard(queens, n))
        else:
            for i in range(n):
                diag1 = row - i + n - 1
                diag2 = row + i
                if columns[i] or diagonals1[diag1] or diagonals2[diag2]:
                    continue
                queens[row] = i
                columns[i] = True
                diagonals1[diag1] = True
                diagonals2[diag2] = True
                self.backtrack(solutions, queens, n, row + 1, columns, diagonals1, diagonals2)
                queens[row] = -1
                columns[i] = False
                diagonals1[diag1] = False
                diagonals2[diag2] = False

    def generateBoard(self, queens, n):
        board = []
        for i in range(n):
            row = ['.'] * n
            row[queens[i]] = 'Q'
            board.append(''.join(row))
        return board
