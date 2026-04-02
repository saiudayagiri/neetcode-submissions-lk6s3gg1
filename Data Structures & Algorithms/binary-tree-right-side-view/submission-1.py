# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return []
        queue=[root]
        while queue:
            lent=len(queue)
            for i in range(lent):
                node=queue.pop(0)
                if i==lent-1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res                    
        