class Solution { // this problem would be easy af and not annoying in python
public:
    std::vector<std::string> findRestaurant(std::vector<std::string>& list1, std::vector<std::string>& list2) {
        std::unordered_map<std::string, int> indexSumMap;
        
        for (int i = 0; i < list1.size(); ++i) {
            auto it = std::find(std::begin(list2), std::end(list2), list1[i]);
            if (it != std::end(list2)) {
                int indexSum = i + std::distance(list2.begin(), it);
                indexSumMap[list1[i]] = indexSum;
            }
        }
        
        int minIndexSum = std::numeric_limits<int>::max();
        std::vector<std::string> result;

        for (const auto& pair : indexSumMap) {
            if (pair.second < minIndexSum) {
                minIndexSum = pair.second;
                result.clear();
                result.push_back(pair.first);
            } else if (pair.second == minIndexSum) {
                result.push_back(pair.first);
            }
        }
        
        return result;
    }
};
