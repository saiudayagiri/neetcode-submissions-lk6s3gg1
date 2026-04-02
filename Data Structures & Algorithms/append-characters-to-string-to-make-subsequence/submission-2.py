class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        for r in range(len(s)):
            if i==len(t):
                return 0
            if s[r]==t[i]:
                i+=1
        return len(t)-i
        