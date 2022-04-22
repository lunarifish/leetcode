// 2022-04-22 12:48:38
// Runtime 0ms(100.0%)
// Memory 39.3%(5.2%)

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private void swapNodes(TreeNode node) {
        TreeNode temp = node.left;
        node.left = node.right;
        node.right = temp;
    }
    private void recuInvert(TreeNode node) {
        if(node == null) 
            return;
        else {
            swapNodes(node);
            TreeNode[] branch = {node.left, node.right};
            for(TreeNode next : branch)
                recuInvert(next);
        }
    }
    public TreeNode invertTree(TreeNode root) {
        if(root == null)
            return root;
        else
            recuInvert(root);
        return root;
    }
