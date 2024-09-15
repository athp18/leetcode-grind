class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        # sieve of erastothenes
        primes = [True] * 1005
        primes[0] = primes[1] = False
        for i in range(2, 1001):
            if primes[i]:
                j = i ** 2
                while j <= 1000:
                    primes[j] = False
                    j += i
        
        for i in range(n):
            if i == 0:
                for j in range(1, nums[i]):
                    if primes[nums[i] - j]:
                        nums[i] = j
                        break
            else:
                for j in range(nums[i - 1] + 1, nums[i]):
                    if primes[nums[i] - j]:
                        nums[i] = j
                        break
        
        for k in range(1, n):
            if nums[k - 1] >= nums[k]:
                return False
        return True
            
