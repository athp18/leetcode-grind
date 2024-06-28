"""
This is the algorithm:
Even though we don't have a sorted array, we can leverage a binary search
Basically, the general approach here is to identify the midpoint of the array, and divide the space over and over again
So if the midpoint is greater than the rightmost number, then we shift our left pointer up by 1 (since our solution is going to be towards the midpoint)
Else, the right becomes the midpoint
And finally, we returned the left pointer, which is the minimum of the array
"""
class Solution: # O (nlogn)
    def findMin(self, nums: List[int]) -> int:
        l, r = 0,  len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
