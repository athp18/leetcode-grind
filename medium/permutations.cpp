class Solution {
public:
    std::vector<std::vector<int>> permute(std::vector<int>& nums) {
        std::vector<std::vector<int>> res;
        std::vector<int> path;
        std::vector<bool> used(nums.size(), false);
        dfs(nums, path, used, res);
        return res;
    }

private:
    void dfs(const std::vector<int>& nums, std::vector<int>& path, std::vector<bool>& used, std::vector<std::vector<int>>& res) {
        // Base case: if the path length is equal to the input nums length
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        for (size_t i = 0;i < nums.size();i++) {
            if (!used[i]) {
                used[i] = true;
                path.push_back(nums[i]);
                dfs(nums, path, used, res);
                path.pop_back();
                used[i] = false;
            }
        }
    }
};
