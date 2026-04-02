class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=len(s)-1
        while s[r]==" ":
            r-=1
        for j in range(r,-1,-1):
            if s[j]==" ":
                return r-j
        return r+1
        