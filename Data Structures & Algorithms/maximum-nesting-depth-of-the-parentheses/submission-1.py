class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        maxi=0
        for c in s:
            if c=="(":
                maxi+=1
            elif c==")":
                maxi-=1
            res=max(res,maxi)
        return res
        