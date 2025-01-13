class Solution:
    def numberOfWays(self, s: str) -> int:
        if not s or len(s) < 3:
            return 0
        
        n = len(s)
        zeros = [0] * (n + 1)  # count zeros up to index i-1
        ones = [0] * (n + 1)   # count ones up to index i-1
        # were looking for the middle index here so we have to allocate an extra index
        
        for i in range(n):
            zeros[i+1] = zeros[i]
            ones[i+1] = ones[i]
            if s[i] == '0':
                zeros[i+1] = zeros[i] + 1
            if s[i] == '1':
                ones[i+1] = ones[i] + 1
        
        count_010 = count_101 = 0

      # find middle positions
      # a intersect b = a * b, which is how we compute count_010 and count_101 at each iteration
      # you could technically do this entire thing in a single loop, but it requires summing (which is an O(n)) operation at each iteration
      # and brings the time complexity to O(n^2)
      # so we do prefix sum early on to get the number of zeros and ones up to each index and then use the resulting array as a lookup table
      # its more space inefficient but still works better time wise
        for i in range(1, n-1):
            if s[i] == '1':
                zeros_before = zeros[i]
                zeros_after = zeros[n] - zeros[i+1]
                count_010 += zeros_before * zeros_after
            else:
                ones_before = ones[i]
                ones_after = ones[n] - ones[i+1]
                count_101 += ones_before * ones_after
                
        return count_101 + count_010
