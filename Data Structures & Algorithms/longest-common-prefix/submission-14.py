class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            cur=strs[0]
            for st in strs:
                if i==len(st) or st[i]!=cur[i]:
                    return st[:i]
                
        return strs[0]