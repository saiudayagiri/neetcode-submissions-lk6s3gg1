class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for j in range(len(t)):
            if i==len(s):
                return True
            if  t[j]==s[i]:
                i+=1
        return i==len(s)
        def rec(i,j):
            if i == len(s):
                return True
            if j== len(t):
                return False
            if s[i]==t[j]:
                return rec(i+1,j+1)
            return rec(i,j+1)
        return rec(0, 0)
        
        i=0
        for j in range(len(t)):
            if i==len(s):
                return True
            if  t[j]==s[i]:
                i+=1
        return i==len