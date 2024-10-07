// In this solution, we use a read and write pointer
// Our right pointer iterates through the string, our left pointer keeps track of where to write the next character
// We iterate through the string with the right pointer
// We copy the character at right pointer to the position at the left pointer
// Then we check if this new character forms a removable substring ("AB" or "CD") with the previous character
// If it does, we move the left pointer back by 2, effectively "erasing" the substring
// If it doesn't, we increment left to be ready for the next character
// I use C++ here since strings in Python are immutable but not in C++
class Solution {
public:
    int minLength(string s) {
        int l = 0;  // Write pointer
        
        for (int r = 0; r < s.length(); r++) {
            s[l] = s[r];
            
            if (l > 0 && 
                ((s[l] == 'B' && s[l-1] == 'A') || 
                 (s[l] == 'D' && s[l-1] == 'C'))) {
                l -= 2;  // Remove the substring by moving write pointer back
            }
            
            l++;
        }
        
        return l;  // Length of the resulting string
    }
};
