class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for r in range(len(t)):
            if i < len(s) and t[r] == s[i]:
                i += 1
        return i == len(s)
        