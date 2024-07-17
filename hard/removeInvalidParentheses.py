from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        if not s:
            return [""]
        
        res = []
        queue = deque([s])
        visited = set([s])
        found = False

        while queue:
            cur = len(queue)
            curres = []
            for _ in range(cur):
                current_string = queue.popleft()
                if isValid(current_string):
                    curres.append(current_string)
                    found = True
                if not found:
                    for i in range(len(current_string)):
                        if current_string[i] in '()':
                            next_string = current_string[:i] + current_string[i + 1:]
                            if next_string not in visited:
                                visited.add(next_string)
                                queue.append(next_string)
            if found:
                res.extend(curres)
                break
        
        return res
