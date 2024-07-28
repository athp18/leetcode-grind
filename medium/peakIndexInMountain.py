class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r-l) // 2
            if arr[mid] > arr[mid+1]: # we're in the decreasing part of the array, so we need to "shift" back
                r = mid
            else: # we're in the increasing part of the array, so we increment by 1
                l = mid + 1
        return l
