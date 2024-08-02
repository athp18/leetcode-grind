class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        start, end = 0, 10

        if len(s) < 10:
            return []

        while end <= len(s):
            curr = s[start:end]
            if curr in seen:
                seen[curr] += 1
            else:
                seen[curr] = 1
            start += 1
            end += 1
        
        res = []

        for key, val in seen.items():
            if val > 1:
                res.append(key)

        return res
