class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        cur=strs[0]
        for i in range(len(cur)):
            for string in strs:
                if i>=len(string) or string[i]!=cur[i]:
                    return string[:i]
                
        return cur
        