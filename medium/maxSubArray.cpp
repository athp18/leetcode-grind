#include <vector>
#include <algorithm>
#include <limits>
// implementing kadane's algorithm
// only update current sum if it gets larger
// O(n) time complexity, O(n) space complexity
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int best_sum = nums[0];
        int current_sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            current_sum = std::max(nums[i], current_sum + nums[i]);
            best_sum = std::max(current_sum, best_sum);
        }
        return best_sum;
    }
};

// lets try an O(n log n) time complexity approach

class Solution1 {
public:
    int maxSubArray(std::vector<int>& nums) {
        return maxSubArrayHelper(nums, 0, nums.size() - 1);
    }

private:
    int maxSubArrayHelper(const std::vector<int>& nums, int left, int right) {
        if (left == right) {
            // Base case: only one element
            return nums[left];
        }

        int mid = left + (right - left) / 2;
        int leftMax = maxSubArrayHelper(nums, left, mid);
        int rightMax = maxSubArrayHelper(nums, mid + 1, right);
        int crossMax = maxCrossingSum(nums, left, mid, right);

        // Return the maximum of the three cases
        return std::max({leftMax, rightMax, crossMax});
    }

    int maxCrossingSum(const std::vector<int>& nums, int left, int mid, int right) {
        int leftSum = std::numeric_limits<int>::min();
        int rightSum = std::numeric_limits<int>::min();
        int sum = 0;

        // Include elements on the left of mid
        for (int i = mid; i >= left; --i) {
            sum += nums[i];
            if (sum > leftSum) {
                leftSum = sum;
            }
        }

        sum = 0;

        // Include elements on the right of mid
        for (int i = mid + 1; i <= right; ++i) {
            sum += nums[i];
            if (sum > rightSum) {
                rightSum = sum;
            }
        }

        // Return sum of elements on the left and right of mid
        return leftSum + rightSum;
    }
};
