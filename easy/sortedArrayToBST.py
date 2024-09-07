# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return TreeNode()
        n = len(nums)
        def helper(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = helper(l, mid-1)
            node.right = helper(mid+1, r)

            return node
        return helper(0, n - 1)
