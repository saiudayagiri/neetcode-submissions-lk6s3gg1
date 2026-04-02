class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        temp=strs[0]
        res=strs[0]
        for i in range(len(temp)):
            for string in strs:
                if i>=len(string) or string[i]!=temp[i]:
                    return temp[:i]
        return res
        