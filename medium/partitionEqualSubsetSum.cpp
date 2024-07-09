class Solution {
public:
    bool canPartition(std::vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        if (total % 2 != 0) {
            return false;
        }
        int target = total / 2;
        int n = nums.size();
        std::vector<std::vector<int>> memo(n, std::vector<int>(target + 1, -1));

        std::function<bool(int, int)> _can_partition = [&](int current_index, int current_sum) -> bool {
            if (current_sum == target) {
                return true;
            }
            if (current_sum > target || current_index >= n) {
                return false;
            }
            if (memo[current_index][current_sum] != -1) {
                return memo[current_index][current_sum];
            }
            bool include_current = _can_partition(current_index + 1, current_sum + nums[current_index]);
            bool exclude_current = _can_partition(current_index + 1, current_sum);
            memo[current_index][current_sum] = include_current || exclude_current;
            return memo[current_index][current_sum];
        };
        
        return _can_partition(0, 0);
    }
};
