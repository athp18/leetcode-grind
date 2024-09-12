class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',  
            ']': '[',
            '}': '{'
        }

        stack = []
        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
