class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # handles empty list
            return ""
        
        prefix = strs[0]
        i=0
        while i<len(prefix):
            for s in strs[1:]:
                if i >= len(s) or s[i] != prefix[i]:
                    return prefix[:i]
            i+=1
        return prefix
