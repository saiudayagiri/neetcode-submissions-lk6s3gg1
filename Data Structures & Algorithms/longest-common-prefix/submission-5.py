class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        lcp = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(lcp) and i < len(s) and lcp[i] == s[i]:
                i += 1
            lcp = lcp[:i]
            if not lcp:
                break
        return lcp
        