class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid = len(nums) // 2
        if nums[mid] > target:
            return self.search(nums[:mid], target)
        elif nums[mid] < target:
            res = self.search(nums[mid+1:], target)
            if res == -1:
                return -1
            else:
                return mid + 1 + res #indices get messed up
        elif nums[mid] == target:
            return mid
        else:
            return -1
