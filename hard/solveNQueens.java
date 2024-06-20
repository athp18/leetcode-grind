import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> solutions = new ArrayList<>();
        int[] queens = new int[n];
        boolean[] columns = new boolean[n];
        boolean[] diagonals1 = new boolean[2 * n - 1];
        boolean[] diagonals2 = new boolean[2 * n - 1];
        backtrack(solutions, queens, n, 0, columns, diagonals1, diagonals2);
        return solutions;
    }

    private void backtrack(List<List<String>> solutions, int[] queens, int n, int row,
                           boolean[] columns, boolean[] diagonals1, boolean[] diagonals2) {
        if (row == n) {
            solutions.add(generateBoard(queens, n));
        } else {
            for (int i = 0; i < n; i++) {
                int diag1 = row - i + n - 1;
                int diag2 = row + i;
                if (columns[i] || diagonals1[diag1] || diagonals2[diag2]) {
                    continue;
                }
                queens[row] = i;
                columns[i] = true;
                diagonals1[diag1] = true;
                diagonals2[diag2] = true;
                backtrack(solutions, queens, n, row + 1, columns, diagonals1, diagonals2);
                queens[row] = -1;
                columns[i] = false;
                diagonals1[diag1] = false;
                diagonals2[diag2] = false;
            }
        }
    }

    private List<String> generateBoard(int[] queens, int n) {
        List<String> board = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char[] row = new char[n];
            for (int k = 0; k < n; k++) {
                row[k] = '.';
            }
            row[queens[i]] = 'Q';
            board.add(new String(row));
        }
        return board;
    }
}
