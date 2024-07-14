//im cooked if i get this problem in an interview
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.empty()) {
            return;
        }
        // transpose matrix
        int n = matrix.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                std::swap(matrix[i][j], matrix[j][i]);
            }
        }
        for (auto& row : matrix) {
            std::reverse(row.begin(), row.end());
        }
    }
};
