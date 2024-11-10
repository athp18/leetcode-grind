# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Memoization dictionary to store results
        # Key: (start, end) tuple representing the range of values
        # Value: List of possible BST roots for that range
        dp = {}
        
        def generateTreesInRange(start, end):
            # Base case: empty range
            if start > end:
                return [None]
            
            # Check if result is already memoized
            if (start, end) in dp:
                return dp[(start, end)]
            
            res = []
            
            # Try each value as the root
            for root_val in range(start, end + 1):
                # Generate all possible left and right subtrees
                left_subtrees = generateTreesInRange(start, root_val - 1)
                right_subtrees = generateTreesInRange(root_val + 1, end)
                
                # Create trees with all combinations of left and right subtrees
                for l in left_subtrees:
                    for r in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = l
                        root.right = r
                        res.append(root)
            
            # Memoize and return result
            dp[(start, end)] = res
            return res
        
        if n == 0:
            return []
            
        return generateTreesInRange(1, n)
