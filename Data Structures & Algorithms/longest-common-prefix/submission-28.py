class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(len(res)):
            for string in strs:
                if i >= len(string) or string[i] != res[i]:
                    return string[:i]
        return res
        