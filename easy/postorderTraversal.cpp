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
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == NULL) {
            return std::vector<int>();
        }
        std::vector<int> result;
        std::vector<int> leftTraverse = postorderTraversal(root->left);
        std::vector<int> rightTraverse = postorderTraversal(root->right);
        result.insert(result.end(), leftTraverse.begin(), leftTraverse.end());
        result.insert(result.end(), rightTraverse.begin(), rightTraverse.end());
        result.push_back(root->val);
        return result;
    }
};
