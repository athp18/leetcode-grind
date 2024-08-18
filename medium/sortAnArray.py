class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)// 2
        l, r = nums[:mid], nums[mid:]
        l = self.sortArray(l)
        r = self.sortArray(r)

        return self.merge(l, r)
    def merge(self, l, r):
        res = []
        i = j = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        
        res.extend(l[i:])
        res.extend(r[j:])
        
        return res
