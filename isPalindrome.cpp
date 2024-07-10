// being able to solve this problem in like 5 min with a 2 pointer approach was ego boosting
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;
        while (l < r) {
            if (!std::isalnum(s[l])) {
                l += 1;
            } else if (!std::isalnum(s[r])) {
                r -= 1;
            } else if (std::tolower(s[l]) != std::tolower(s[r])) {
                return false;
            } else {
                l++;
                r--;
            }
        }
        return true;
    }
};
