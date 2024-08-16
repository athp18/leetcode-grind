class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def next_index(i):
            return (i + nums[i]) % n
        
        def detect_cycle(start):
            slow = fast = start
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
                slow = next_index(slow)
                fast = next_index(next_index(fast))
                if slow == fast:
                    if slow == next_index(slow):
                        return False  # Loop of size 1
                    return True
            return False
        
        for i in range(n):
            if nums[i] == 0:
                continue
            if detect_cycle(i):
                return True
        
        return False
