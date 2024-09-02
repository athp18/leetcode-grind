# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # okay this one was lowkey hard as fuck and aids as fuck. but hey, commit 300 lol
    def maxSumBST(self, root: TreeNode) -> int:
        self.max_sum = 0
        
        def dfs(node):
            if not node:
                return float('inf'), float('-inf'), 0, True
            
            left_min, left_max, left_sum, left_is_bst = dfs(node.left)
            right_min, right_max, right_sum, right_is_bst = dfs(node.right)
            
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, curr_sum)
                return min(left_min, node.val), max(right_max, node.val), curr_sum, True
            
            return float('-inf'), float('inf'), 0, False
        
        dfs(root)
        return self.max_sum
