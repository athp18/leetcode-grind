# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time and space complexit

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # guys im fucked
        # blind 75
        res = [root.val]
        def dfs(root): ## depth first search
            if not root:
                return 0
            leftMax = dfs(root.left) #dfs the left subtree
            rightMax = dfs(root.right) #dfs the right subtree
            leftMax = max(leftMax, 0) # identify the max of the left
            rightMax = max(rightMax, 0) # identify the max of the right
            res[0] = max(res[0], root.val+leftMax+rightMax) # append the max path sum
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
