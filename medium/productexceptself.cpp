#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int length = nums.size();
        std::vector<int> output(length, 1);
        std::vector<int> prefix_products(length, 1);
        std::vector<int> postfix_products(length, 1);
        
        for (int i = 1; i < length; ++i) {
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1];
        }
        for (int i = length - 2; i >= 0; --i) {
            postfix_products[i] = postfix_products[i + 1] * nums[i + 1];
        }
        for (int i = 0; i < length; ++i) {
            output[i] = prefix_products[i] * postfix_products[i];
        }
        
        return output;
    }
};
