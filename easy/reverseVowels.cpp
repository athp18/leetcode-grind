class Solution {
public:
    std::string reverseVowels(std::string s) {
        if (s.empty()) {
            return s;
        }
        
        int l = 0;
        int r = s.size() - 1;
        
        std::string vowels = "aeiouAEIOU";
        
        while (l < r) {
            // Condition one: both l and r are in vowels
            if (inVowels(s[l], vowels) && inVowels(s[r], vowels)) {
                std::swap(s[l], s[r]);
                l += 1;
                r -= 1;
            } else if (inVowels(s[l], vowels)) { // Condition two: left pointer in vowels, but not right (we move up down the right pointer, check again)
                r -= 1;
            } else if (inVowels(s[r], vowels)) { // condiiton three: right pointer in vowels, but not left (we move down the left pointer, check again)
                l += 1;
            } else { // neither in vowels: move both
                l += 1;
                r -= 1;
            }
        }
        
        return s;
    }
    
private:
    bool inVowels(char c, const std::string& str) { // helper function because its annoying to write that out each time
        return str.find(c) != std::string::npos;
    }
};
