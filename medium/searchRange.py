class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def findLast(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
        
        first = findFirst(nums, target)
        last = findLast(nums, target)
        
        #binary search time
        if first <= last:
            return [first, last]
        else:
            return [-1, -1]
