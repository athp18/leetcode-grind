class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Sort the input array
        std::sort(nums.begin(), nums.end());
        
        std::vector<std::vector<int>> result;
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); ++i) {
            // Skip duplicates for i
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            
            // Early termination if current number is positive
            if (nums[i] > 0) {
                break;
            }
            
            int l = i + 1;
            int r = nums.size() - 1;
            
            while (l < r) {
                long long threeSum = static_cast<long long>(nums[i]) + nums[l] + nums[r];
                
                if (threeSum > 0) {
                    r--;
                }
                else if (threeSum < 0) {
                    l++;
                }
                else {
                    result.push_back({nums[i], nums[l], nums[r]});
                    
                    // Skip duplicates for l and r
                    while (l < r && nums[l] == nums[l+1]) l++;
                    while (l < r && nums[r] == nums[r-1]) r--;
                    
                    l++;
                    r--;
                }
            }
        }
        return result;
    }
};
