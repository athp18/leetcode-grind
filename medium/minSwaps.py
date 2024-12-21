class Solution:
    def minSwaps(self, s: str) -> int:
        def count_min_swaps(s):
            count_ones = s.count('1')
            count_zeros = len(s) - count_ones

            if abs(count_ones - count_zeros) > 1:
                return -1
                
            mismatch_start_one, mismatch_start_zero = 0, 0

            for i in range(len(s)):
                if i % 2 == 0: 
                    if s[i] == '1':
                        mismatch_start_zero += 1
                    else:
                        mismatch_start_one += 1
                else:  
                    if s[i] == '1':
                        mismatch_start_one += 1
                    else:
                        mismatch_start_zero += 1
            
            if count_ones > count_zeros:
                return mismatch_start_one // 2
            if count_zeros > count_ones:
                return mismatch_start_zero // 2
            return min(mismatch_start_zero, mismatch_start_one) // 2
        return count_min_swaps(s)
