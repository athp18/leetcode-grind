class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                score = stack.pop()
                if score == 0:
                    score = 1
                else:
                    score *= 2
                stack[-1] += score
        return stack[0]
