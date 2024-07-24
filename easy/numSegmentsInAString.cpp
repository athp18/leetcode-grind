class Solution {
public:
    int countSegments(string s) {
        int count = 0;
        bool inSegment = false;
        
        for (char c : s) {
            if (isspace(c)) {
                inSegment = false;
            } else {
                if (!inSegment) {
                    count++;
                }
                inSegment = true;
            }
        }
        
        return count;
    }
};
