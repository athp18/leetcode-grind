class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        int start = 0;
        int n = nums.size();
        vector<std::string> output;
        while (start < n) {
            int end = start;
            while (end + 1 < n && nums[end+1] == nums[end] + 1) {
                end += 1;
            }
            output.push_back(helper(start, end, nums));
            start = end + 1;
        }
        return output;
    }
private:
    std::string helper(int s, int e, vector<int>& nums) {
        if (s == e) {
            return std::to_string(nums[e]);
        } else {
            return std::to_string(nums[s]) + "->" + std::to_string(nums[e]);
        }
    }
};
