class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if sum(nums) == 0: # base case
            return 0
        
        """
        This is a very naive approach.
        Essentially, we use a while loop with condition being that the sum of nums is > 0. While that condition holds true,
        we increment a total variable by 1. Meanwhile, we subtract a temporary min from each number in nums if that num is greater
        than 0. This is O(n^2), since we take sum (O(n)) in each iteration of the while loop, and there are n iterations.
        
        total = 0
        while sum(nums) > 0:
            curr = min(x for x in nums if x > 0)
            nums = [num - curr if num > 0 else 0 for num in nums]
            total += 1
        return total
        """

        """
        a more optimized approach is just using a set

        here, we filter out nums so that it only consists of positive numbers, then convert it to a set to get the number of unique
        numbers. the length of that set represents the number of operations we need to do.
        """
        res = set(x for x in nums if x > 0)
        return len(res)
