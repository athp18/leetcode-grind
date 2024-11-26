class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        first = {}
        last = {}

        # Populate the dictionaries
        for i in range(len(nums)):
            # Update frequency
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            # Update last occurrence
            last[nums[i]] = i
            # Store first occurrence only if we haven't seen this number before
            if nums[i] not in first:
                first[nums[i]] = i
        
        # Find the degree (maximum frequency)
        degree = max(freq.values())

        # Find the shortest subarray length among numbers with maximum frequency
        min_len = len(nums)
        for n in freq:
            if freq[n] == degree:
                curr_len = last[n] - first[n] + 1
                min_len = min(min_len, curr_len)
        return min_len
