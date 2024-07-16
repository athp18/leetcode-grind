class Solution {
public:
    string customSortString(string order, string s) {
        std::unordered_map<char, int> hashmap;
        for (char c : s) {
            hashmap[c]++;
        }
        std::string result;
        for (char c : order) {
            if (hashmap.find(c) != hashmap.end()) {
                result.append(hashmap[c], c);
                hashmap.erase(c); // make sure to do this
            }
        }
        for (const auto& pair : hashmap) {
            result.append(pair.second, pair.first);
        }
        return result;
    }
};
