class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows <= 1 or len(s) <= numRows:
            return s
        
        res = ""
        cycle = 2 * numRows - 2 
        
        for i in range(numRows):
            for j in range(i, len(s), cycle):
                res += s[j]
                
                zigIndex = j + cycle - (2 * i)
                if i != 0 and i != numRows - 1 and zigIndex < len(s):
                    res += s[zigIndex]
                    
        return res
