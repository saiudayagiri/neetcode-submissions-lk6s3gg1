class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        longest=strs[0]
        for i in range(len(longest)):
            for string in strs:
                if i>=len(string) or string[i]!=longest[i]:
                    return longest[:i]
        return longest
        