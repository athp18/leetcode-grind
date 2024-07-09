class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int best_product = nums[0];
        int max_product = nums[0];
        int min_product = nums[0];
        
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < 0) {
                std::swap(max_product, min_product);
            }
            
            max_product = std::max(nums[i], max_product * nums[i]);
            min_product = std::min(nums[i], min_product * nums[i]);
            
            best_product = std::max(best_product, max_product);
        }
        
        return best_product;
    }
};
// this is just modifying max sum subarray which i solved a while ago, but extending it to change the algorithm
// essentially, you add a min product variable, and swap min and max product if its negative
// and best product is iteratively updated
