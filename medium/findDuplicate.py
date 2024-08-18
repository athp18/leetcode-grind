class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # reminder for me
        # floyds cycle detection

        # two fast pointers: slow and fast. fast moves 2x slow
        slow, fast = 0, 0

        while True:
            # in floyd's algorithm each index points to a number. so if a number has multiple indices pointing to it, there's a cycle
            slow = nums[slow] # slow pointer -- initialize at the number of its index (initially 0)
            fast = nums[nums[fast]] # fast pointer. basically this moves twice at a time 

            if slow == fast: # intersection detected. slow is now at the intersection point
                break
        
        s2 = 0 # start from the start of the array
        while True:
            slow = nums[slow] # move over and over
            s2 = nums[s2]
            if slow == s2:
                return s2 # return either
