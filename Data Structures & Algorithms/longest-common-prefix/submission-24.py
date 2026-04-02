class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(len(strs[0])):
            for string in strs:
                if i >= len(string) or ans[i] != string[i]:
                    return ans[:i]
        return ans
        