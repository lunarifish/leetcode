// 2022-05-23 11:40:51
// Runtime 0ms(100.0%)
// Memory 8.3mb(18.7%)

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
    vector<int> ret;
    void backtrack(TreeNode* root) {
        if (!root)
            return;
        else {
            ret.push_back(root->val);
            backtrack(root->left);
            backtrack(root->right);
        }
    }
    vector<int> preorderTraversal(TreeNode* root) {
        backtrack(root);
        return ret;
    }
};
