from collections import deque

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        #dequeu
        queue = deque([(0,0,1)])
        seen = set([0,0,1])
        while queue:
            m, p, s = queue.popleft()

            if p == target:
                return m

            queue.append((m + 1, p+s, 2*s))

            if (p + s > target and s > 0) or (p +s < target and s < 0):
                queue.append((m+1, p, -s/abs(s)))
        return 0
