/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }
private:
    int dfs(TreeNode* node, int maxval) {
        if (node == nullptr) { // recursive dfs
            return 0;
        }
        int res = 0;
        if (node->val >= maxval) { 
            res = 1;
        }
        maxval = std::max(maxval, node->val);
        res += dfs(node->left, maxval);
        res += dfs(node->right, maxval);
        return res;
    }
};
