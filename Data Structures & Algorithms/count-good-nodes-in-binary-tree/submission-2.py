# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,ms):
            nonlocal cnt
            if not node:
                return
            if node.val>=ms:
                cnt+=1
                ms=node.val
            dfs(node.left,ms)
            dfs(node.right,ms)
        cnt=0
        dfs(root,root.val)
        return cnt
        