// 2022-05-27 19:33:59
// Runtime 0ms(100.0%)
// Memory 8.2mb(30.1%)

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
            backtrack(root->left);
            ret.push_back(root->val);
            backtrack(root->right);
        }
    }
    vector<int> inorderTraversal(TreeNode* root) {
        backtrack(root);
        return ret;
    }
};
