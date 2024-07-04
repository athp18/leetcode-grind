// Re-reference this later

class Solution {
public:
    bool exist(std::vector<std::vector<char>>& board, std::string word) {
        int rows = board.size();
        int cols = board[0].size();
        
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (board[row][col] == word[0] && dfs(board, word, row, col, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

private:
    bool dfs(std::vector<std::vector<char>>& board, const std::string& word, int r, int c, int index) {
        if (index == word.size()) {
            return true;
        }
        if (r < 0 || c < 0 || r >= board.size() || c >= board[0].size() || board[r][c] != word[index]) {
            return false;
        }

        char tmp = board[r][c];
        board[r][c] = '#';  // marked as visited

        bool found = dfs(board, word, r + 1, c, index + 1) ||
                     dfs(board, word, r - 1, c, index + 1) ||
                     dfs(board, word, r, c + 1, index + 1) ||
                     dfs(board, word, r, c - 1, index + 1);

        board[r][c] = tmp; 

        return found;
    }
};
