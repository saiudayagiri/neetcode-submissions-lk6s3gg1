# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, ms, cnt):
            if not node:
                return
            if node.val >= ms:  # Include equal condition
                cnt[0] += 1  # Use list to keep track of count
                ms = node.val  # Update max_so_far
            
            dfs(node.left, ms, cnt)
            dfs(node.right, ms, cnt)
        
        cnt = [0]  # Using a list to track count
        dfs(root, root.val, cnt)
        return cnt[0]
        