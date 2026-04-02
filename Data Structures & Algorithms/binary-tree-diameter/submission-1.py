# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0   # store the max diameter

        def height(node):
            nonlocal diameter
            if not node:
                return 0
            # compute left and right subtree heights
            left_h = height(node.left)
            right_h = height(node.right)
            
            # update diameter if this path is longer
            diameter = max(diameter, left_h + right_h)
            
            # return height of this subtree
            return 1 + max(left_h, right_h)
        
        height(root)
        return diameter
