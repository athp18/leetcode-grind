class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
    
        for i in range(n):
            max_digit = '0'
            max_idx = i
            for j in range(i + 1, n):
                if nums[j] >= max_digit:
                    max_digit = nums[j]
                    max_idx = j
        
            if max_digit > nums[i]:
                nums[i], nums[max_idx] = nums[max_idx], nums[i]
                return int(''.join(nums))

        return num
