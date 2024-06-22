#include <iostream>
#include <vector>

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int length = nums.size();
        int expected = (length * (length + 1)) / 2;
        int actual = std::accumulate(nums.begin(), nums.end(), 0);
        return expected - actual;
    }
};
