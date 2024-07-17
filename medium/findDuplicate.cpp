class Solution {
public:
    int findDuplicate(std::vector<int>& nums) {
        std::set<int> seen;
        for (int n : nums) {
            if (seen.find(n) != seen.end()) {
                return n;
            } else {
                seen.insert(n);
            }
        }
        return -1;
    }
};
