class Solution {
public:
    std::vector<int> intersection(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::set<int> res;
        if (nums2.size() < nums1.size()) {
            std::swap(nums2, nums1);
        }

        for (const auto& num : nums1) {
            if (std::find(nums2.begin(), nums2.end(), num) != nums2.end()) {
                res.insert(num); 
            }
        }
        return std::vector<int>(res.begin(), res.end());
    }
};
