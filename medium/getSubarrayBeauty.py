class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res = [0] * (len(nums) - k + 1)
        counter = [0] * 50

        for i in range(len(nums)):
            if nums[i] < 0:
                counter[nums[i] + 50] += 1
            if i - k >= 0 and nums[i - k] < 0:
                counter[nums[i-k] + 50] -= 1
            if (i - k + 1) >= 0:
                count = 0
                for j in range(50):
                    count += counter[j]
                    if count >= x:
                        res[i-k+1] = j - 50
                        break
        
        return res
