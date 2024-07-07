// kept my streak lol
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string longestPalindrome(string s) {
    int n = s.size();
    if (n == 0) return "";
    
    // dp[i][j] will be true if the string from index i to j is a palindrome
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    
    int start = 0; // To store the starting index of the longest palindromic substring
    int maxLength = 1; // To store the length of the longest palindromic substring
    
    // All substrings of length 1 are palindromes
    for (int i = 0; i < n; i++) {
        dp[i][i] = true;
    }
    
    // Check for sub-strings of length 2
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == s[i + 1]) {
            dp[i][i + 1] = true;
            start = i;
            maxLength = 2;
        }
    }
    
    // Check for lengths greater than 2
    for (int len = 3; len <= n; len++) {
        for (int i = 0; i < n - len + 1; i++) {
            int j = i + len - 1;
            if (dp[i + 1][j - 1] && s[i] == s[j]) {
                dp[i][j] = true;
                start = i;
                maxLength = len;
            }
        }
    }
    
    return s.substr(start, maxLength);
}
