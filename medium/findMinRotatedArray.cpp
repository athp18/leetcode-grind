class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0;
        int r = nums.size() - 1;

        while (l < r) {
            int mid = (l + r) / 2; 
            if (nums[mid] > nums[r]) { 
                l = mid + 1; 
                // this means we're in the decreasing part of the array, which is where we want to be
                // now we binary search this part
            } else if (nums[mid] > nums[l]) {
                // this means we're in the increasing part of the array
                r = mid;
            } else { 
                r--;
                // to properly handle duplicates
            }
        }
        return nums[l];
    }
};
