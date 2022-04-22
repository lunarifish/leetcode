# 2022-04-22 12:28:40
# Runtime 32ms(89.2%)
# Memory 15mb(21.6%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        
        def recuInvert(node):
            if node is None:
                return
            else:
                temp = node.right
                node.right = node.left
                node.left = temp
                for i in [node.left, node.right]:
                    recuInvert(i)
        recuInvert(root)
        return root
