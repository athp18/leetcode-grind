class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        std::map<int, int> hashmap;
        for (int k : nums) {
            if (hashmap.find(k) != hashmap.end()) {
                hashmap[k] += 1;
            } else {
                hashmap[k] = 1;
            }
        }
        int a = 0;
        for (const auto& [key, value] : hashmap) {
            if (value > n / 2) {
                a = key;
            }
        }
        return a;
    }
};
