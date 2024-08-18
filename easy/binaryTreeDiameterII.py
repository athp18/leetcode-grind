class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True] # global var in case of issue

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)

            if balanced[0] == False:
                return 0

            r = dfs(node.right)

            if abs(l - r) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(l, r)
        dfs(root)
        return balanced[0]
      # time o(n), space o(n)
