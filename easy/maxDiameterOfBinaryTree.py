class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)

            self.diameter = max(self.diameter, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        dfs(root)
        return self.diameter
