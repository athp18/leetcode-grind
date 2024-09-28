class Solution:
  # initially, my approach was to use a hashmap for O(1) lookup, however creating the hashmap is actually less efficient than binary search, which is O(log n)
  # this has O(n) time complexity and O(1) space complexity
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        assert len(nums1) == len(nums2)

        if sorted(nums1) == sorted(nums2): # nums1 and nums2 is the same
            return 0
        nums = sorted(nums1)
        initial_sum = 0
        for i in range(len(nums1)):
            initial_sum += abs(nums1[i]-nums2[i])
        initial_sum %= 10**9 + 7

        mrdx = 0
        for i, j in zip(nums1, nums2):
            curr = abs(i-j)
            a = self.binary_search(nums, j)
            potential = float('inf')
            if a < len(nums):
                potential = abs(nums[a] - j)
            if a:
                potential = min(potential, abs(nums[a-1]-j))
            mrdx = max(mrdx, curr - potential)
        
        return (initial_sum - mrdx) % (10**9 + 7)
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        return left
