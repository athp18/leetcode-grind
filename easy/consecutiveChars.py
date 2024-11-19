class Solution:
    def maxPower(self, s: str) -> int:
        curr_len = 1
        max_len = 1
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                curr_len += 1
            else:
                curr_len = 1
            max_len = max(max_len, curr_len)
        return max_len
