#include <vector>
#include <set>
#include <algorithm>

class Solution {
public:
    int longestConsecutive(std::vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        
        std::set<int> s(nums.begin(), nums.end());
        std::vector<int> vec(s.begin(), s.end());
    
        int max_length = 1;
        int current_length = 1;
        
        for (int i = 1; i < vec.size(); i++) {
            if (vec[i] - vec[i-1] == 1) {
                current_length += 1;
            } else if (vec[i] != vec[i-1]) {
                current_length = 1;
            }
            if (current_length > max_length) {
                max_length = current_length;
            }
        }
        
        return max_length;
    }
};
