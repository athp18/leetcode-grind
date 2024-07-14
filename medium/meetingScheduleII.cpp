/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */


class Solution {
public:
    int minMeetingRooms(std::vector<Interval>& intervals) {
        // sort based on start times
        std::sort(intervals.begin(), intervals.end(), 
                  [](const Interval& a, const Interval& b) {
                      return a.start < b.start;
                  });
        
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        
        for (const auto& interval : intervals) {
            if (!pq.empty() && interval.start >= pq.top()) {
                pq.pop();
            }
            pq.push(interval.end);
        }
        return pq.size();
    }
};
