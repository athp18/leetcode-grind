#include <vector>
#include <string>
// O(3^K) time complexity lol
// O(K) space complexity (since a temp board is created of size K)

class Solution {
public:
    bool exist(std::vector<std::vector<char>>& board, std::string word) {
        int rows = board.size();
        int cols = board[0].size();
        
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (backtrack(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
    
private:
    bool backtrack(std::vector<std::vector<char>>& board, const std::string& word, int r, int c, int index) {
        if (index == word.length()) {
            return true;
        }
        
        if (r < 0 || r >= board.size() || c < 0 || c >= board[0].size() || board[r][c] != word[index]) {
            return false;
        }
        char temp = board[r][c]; // mark as visited
        board[r][c] = '#';

        bool result = (backtrack(board, word, r + 1, c, index + 1) ||
                       backtrack(board, word, r - 1, c, index + 1) ||
                       backtrack(board, word, r, c + 1, index + 1) ||
                       backtrack(board, word, r, c - 1, index + 1));
        board[r][c] = temp;
        return result;
    }
};
