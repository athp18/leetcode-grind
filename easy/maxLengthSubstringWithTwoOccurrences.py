class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        l, MAX = 0, 0

        for r in range(len(s)):
            hashmap[s[r]] += 1
            while hashmap[s[r]] > 2:
                hashmap[s[l]] -= 1
                l += 1
            MAX = max(MAX, r - l + 1)
        return MAX
