class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size(); // n = length of nums
        std::map<int, int> hashmap; // hashmap for constant time access to element
        for (int k : nums) { // iterate over each element in nums
            if (hashmap.find(k) != hashmap.end()) { // if its in the hashmap, increase the count of the element by 1
                hashmap[k] += 1;
            } else {
                hashmap[k] = 1; // else its been seen for the first time->boost count by 1
            }
        }
        int a = 0; // a is our result variable; we initialize as 0
        for (const auto& [key, value] : hashmap) { //iterate over keys and values in the hashmap
            if (value > n / 2) { // if the value is the majority element, we set it to a
                a = key; // set it to a
            }
        }
        return a; // return a. we dont have to worry about if there is no majority element since its always guaranteed
    }
};
