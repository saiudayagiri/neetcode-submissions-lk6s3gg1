class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        cur=strs[0]
        for i in range(len(cur)):
            for string in strs:
                if i>=len(string) or string[i]!=cur[i]:
                    return cur[:i]
        return cur

        