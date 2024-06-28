// To do: go back and edit this. Rn this solution is O(n^2) and i want to get it down to O(n)
#include <iostream>
#include <vector>

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        std::vector<int> output(length, 1);
        for (int i = 0; i < nums.size(); i++) {
            int prefix_product = 1;
            for (int k = 0; k < i; k++) {
                prefix_product *= nums[k];
            }
            int postfix_product = 1;
            for (int j=i+1; j < length; j++) {
                postfix_product *= nums[j];
            }
            output[i] = prefix_product * postfix_product;
        }
        return output;
    }
};
