#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    int lengthOfLongestSubstring(const std::string& s) {
        std::unordered_set<char> charSet;
        for (char c : s) {
            charSet.insert(c);
        }
        if (charSet.size() == 1) {
            return 1;
        }
        std::unordered_map<char, int> hashmap;
        int start = 0;
        int max_length = 0;
      
        for (int i = 0; i < s.size(); ++i) {
            char current_char = s[i];
            if (hashmap.find(current_char) != hashmap.end() && hashmap[current_char] >= start) {
                start = hashmap[current_char] + 1;
            }
            hashmap[current_char] = i;
            max_length = std::max(max_length, i - start + 1);
        }

        return max_length;
    }
};
