class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # simple, efficient, elegant solution
        # basically, the num of operations is sort of like a prefix + postfix sum: we calculate total number of ones and total number of operations
        # to move the ones to the index, and say our array has that sum
        if not boxes: # edge case
            return []
        n = len(boxes) # length
        answer = [0] * n # answer array
        
        ones = 0 # initialize # of ones
        ops = 0 # initialize # of operations
        
        for i in range(n): # forward pass 
            answer[i] += ops # add the number of operations
            if boxes[i] == '1': # increment # of ones by 1 if 1 is seen
                ones += 1
            ops += ones # increment operations by the number of ones
        
        ones = 0 # reset for a backwards pass
        ops = 0
        
        for i in range(n-1, -1, -1): # same idea
            answer[i] += ops
            if boxes[i] == '1':
                ones += 1
            ops += ones
            
        return answer # return the answer array
