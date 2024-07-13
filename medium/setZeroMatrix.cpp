#include <iostream>
#include <set>

//more efficient implementation of set_zero_matrix.py. imo a more efficient solution (less memory complexity) prolly involves just using a boolean but i'm lazy lol
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        std::set<int> row_set;
        std::set<int> col_set;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (matrix[r][c] == 0) {
                    row_set.insert(r);
                    col_set.insert(c);
                }
            }
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (row_set.count(r) != 0 || col_set.count(c) != 0) {
                    matrix[r][c] = 0;
                }
            }
        }
    }
};
