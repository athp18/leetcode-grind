class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPali(s):
            return s == s[::-1]
        def backtrack(start, path):
            if start == len(s):
                res.append(path)
                return
            for i in range(start+1, len(s)+1):
                if checkPali(s[start:i]):
                    backtrack(i, path + [s[start:i]])
        res = []
        backtrack(0, [])
        return res
