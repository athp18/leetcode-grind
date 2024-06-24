class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0) { // edge case: nums is an empty array
            return 0;
        }
        int left = 0; // left pointer -> initialize at 0
        int right = nums.size() - 1; // right pointer -> initialize at the last index
        // Algorithm: Scan through the array with the left and right pointers and perform a binary search. Update left and right depending on the position of our pointers
        // finally return left
        while (left <= right) {
            int mid = left + (right - left) / 2; // midpoint. CHECK: this helps avoid overflow
            if (nums[mid] == target) { // we have found the target: -> return
                return mid;
            } else if (nums[mid] < target) { // target is larger than midpoint -> shift left pointer over by 1
                left += 1;
            } else if (nums[mid] > target) { // target is smaller than midpoint -> shift right pointer down by 1
                right -= 1;
            }
        }
        return left; // return final position of left pointer. In practice this returns the value closest to target
    }
};
