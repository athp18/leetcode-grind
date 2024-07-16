class Solution {
public:
    char findTheDifference(string s, string t) {
        int result = 0;
        for (auto c : s) {
            result ^= static_cast<int>(c);
        }
        for (auto c : t) {
            result ^= static_cast<int>(c);
        }
        return static_cast<char>(result);
    }
};
