class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        SUM = 0
        i, n = 0, len(s)

        while i < n:
            if i < n-1 and hashmap[s[i]] < hashmap[s[i+1]]:
                SUM += hashmap[s[i+1]] - hashmap[s[i]]
                i += 2
            else:
                SUM += hashmap[s[i]]
                i += 1
        return SUM
