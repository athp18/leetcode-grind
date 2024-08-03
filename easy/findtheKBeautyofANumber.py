# this is a pretty simple problem, and i'll explain like this:
# given that the dividend has to be length of k, we can use a sliding window. we initialize the window to k-1
# then, we iterate through the string and if the number is not equal to 0 (which will cause zero division error) and divisible by num, we increment
# our count variable by 1
# finally, we return count
# sliding window uses a while loop a lot: important strategy
# another important strategy; right pointer is the iterator
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        if not num:
            return 0
        l, r = 0, k-1
        count = 0
        n = str(num)
        while r < len(n):
            if int(n[l:r+1]) != 0 and num % int(n[l:r+1]) == 0:
                count += 1
            l += 1
            r += 1
        return count
            
