// 2022-05-23 11:42:31
// Runtime 4ms(40.1%)
// Memory 8.4mb(7.8%)

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
            backtrack(root->right);
            ret.push_back(root->val);
        }
    }
    vector<int> postorderTraversal(TreeNode* root) {
        backtrack(root);
        return ret;
    }
};
