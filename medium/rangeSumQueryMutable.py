class BIT: # use a fenwick tree for O(log n) operations
    def __init__(self, nums): # initialize bit
        self.n = len(nums) + 1 # size of the BIT
        self.bit = [0] * self.n # initialize bit
        for i, num in enumerate(nums): # build BIT of nums
            self.increment(i, num)

    def increment(self, idx, amt): 
        idx += 1 # BITs are 1-indexed (the 0 index throws off the point of 2^n)
        while idx < self.n: # In a Fenwick tree, each node that is a power of 2 represents a prefix sum of the elements before, and including, it. 
          # what we're essentially doing here is calculating the indices that need to be updating and incrementing them iteratively. The range of elements that each node is responsible for is determined by the LSB
            self.bit[idx] += amt
            idx += idx & -idx # add the value of the least significant set bit to the index
          # this has O(log n) time complexity

    def sum(self, e): # prefix sum method
        e += 1 # again: BITs are 1 indexed, so we increment 1
        s = 0 # our sum value
        while e > 0:
            s += self.bit[e] # Add the value at current index to our sum
        # In the increment method, we move forwards through the tree.
        # Here, we're moving backwards, accumulating partial sums.
        # Each self.bit[e] stores a cumulative sum for a specific range.
            e -= e & -e
          # This is the key operation for traversing the Fenwick Tree structure:
        # 1. (e & -e) isolates the least significant set bit of e
        # 2. Subtracting this from e "turns off" this least significant set bit
        # 3. This effectively moves us to the parent node in the tree
        # 4. We continue this process, accumulating sums from all relevant nodes
      # This has O(log n) time complexity
        return s

    def sum_range(self, s, e):
        return self.sum(e) - self.sum(s-1) # pretty simple: to add the range between s and e, we just subtract the prefix sum of s and prefix sum of e

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums # our initial array
        self.bit = BIT(nums) # a BIT representation of our array

   
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]  # Calculate the difference between new and old values
        # We calculate this difference because:
        # 1. The BIT stores cumulative sums, so we need to update by the difference
        # 2. The BIT is 1-indexed, but we want to keep our original array 0-indexed

        self.nums[index] = val  # Update the value in our original array
        
        self.bit.increment(index, diff)  # Update the BIT
        # We pass 'index' directly because the BIT.increment method will handle the 1-indexing internally
  
    def sumRange(self, left: int, right: int) -> int: # self explanatory
        return self.bit.sum_range(left, right)
