class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i=0
        for r in range(len(t)):
            if s[i]==t[r]:
                i+=1
            if i==len(s):
                return True
        return i==len(s)
        