class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for i in range(len(lcp)):
            for string in strs:
                if i >= len(string) or string[i] != lcp[i]:
                    return lcp[:i]
        return lcp
        
        