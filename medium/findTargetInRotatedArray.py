class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # double binary search
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        
class Solution1(object):
    def search(self, nums, target): # second (more simple imo) implementation that just uses logic
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]: # left portion is sorted
                    r = mid -1
                else:
                    l = mid+ 1
            else:
                if nums[mid] < target <= nums[r]: 
                    l = mid + 1 # right half is sorted
                else:
                    r = mid -1
        return -1
