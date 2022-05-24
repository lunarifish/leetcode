// 2022-05-24 09:47:13
// Runtime 0ms(100.0%)
// Memory 9.7mb(41.7%)

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
    bool ret = true;
    void match(TreeNode* root, int val) {
        if (root == NULL)
            return;
        else if (root->val != val) {
            ret = false;
            return;
        }
        else {
            match(root->left, val);
            match(root->right, val);
        }
    }
    bool isUnivalTree(TreeNode* root) {
        match(root, root->val);
        return ret;
    }
};
