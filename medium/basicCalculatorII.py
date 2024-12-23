class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        
        # helper function
        def get_number(i):
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            return num, i
        
        # pass #1 -- multiply/divide (since these are first in pemdas)
        stack = []
        i = 0
        curr_num = 0
        curr_op = '+'
        
        while i < len(s):
            if s[i].isdigit():
                curr_num, i = get_number(i)
                
                if curr_op == '*':
                    stack.append(stack.pop() * curr_num)
                elif curr_op == '/':
                    # division is a little annoying since theres more edge cases but we ball
                    prev = stack.pop()
                    result = abs(prev) // abs(curr_num)
                    if prev * curr_num < 0:
                        result = -result
                    stack.append(result)
                else:
                    # For + and -, just push the number with appropriate sign
                    if curr_op == '+':
                        stack.append(curr_num)
                    else:  # curr_op == '-'
                        stack.append(-curr_num)
                
            elif s[i] in '+-*/':
                curr_op = s[i]
                i += 1

        return sum(stack)
