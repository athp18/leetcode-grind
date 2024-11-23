class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        curr_sum = count = 0
        
        for num in nums:
            curr_sum += num
            
            # Get remainder when current sum is divided by k
            # Using (curr_sum % k + k) % k to handle negative numbers
            remainder = (curr_sum % k + k) % k
            
            # If this remainder exists in our map, it means we have found
            # subarrays with sum divisible by k.
            if remainder in prefix:
                count += prefix[remainder]
            
            # Update the frequency of current remainder
            prefix[remainder] = prefix.get(remainder, 0) + 1
            
        return count
