from collections import deque

class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = deque(nums[:len(nums)//2][::-1])
        r = deque(nums[len(nums)//2:][::-1])

        res = 0

        while len(l) >0 and len(r) > 0:
            if r[0] >= l[0] * 2:
                l.popleft()
                r.popleft()
                res += 1
                continue

            l.popleft()
        return res*2          
        
