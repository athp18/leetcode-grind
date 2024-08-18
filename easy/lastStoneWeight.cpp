#include <iostream>
#include <queue>
#include <vector>

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // use c++ for built in max heap
        std::priority_queue<int> maxHeap(stones.begin(), stones.end());

        while (maxHeap.size() > 1) {
            int first = maxHeap.top();
            maxHeap.pop();
            int second = maxHeap.top();
            maxHeap.pop();

            if (first != second) {
                maxHeap.push(first-second);
            }
        }
        if (maxHeap.empty()) {
            return 0;
        } else {
            return maxHeap.top();
        }
    }
};
