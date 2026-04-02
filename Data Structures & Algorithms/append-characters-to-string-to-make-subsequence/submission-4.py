class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for r in range(len(s)):
            if i < len(t) and s[r] == t[i]:
                i += 1
        return len(t) - i
        