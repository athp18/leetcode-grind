class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start: int, parts: List[str]):
            if len(parts) == 4 and start == len(s):
                result.append('.'.join(parts))
                return
            
            if len(parts) == 4 or start == len(s):
                return
            
            for i in range(start, min(start + 3, len(s))):
                part = s[start:i+1]
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
                parts.append(part)
                backtrack(i + 1, parts)
                parts.pop()
        
        result = []
        backtrack(0, [])
        return result
