class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for k in range(max(len(word1), len(word2))):
            if k < len(word1):
                res += word1[k]
            if k < len(word2):
                res += word2[k]
        return res
        