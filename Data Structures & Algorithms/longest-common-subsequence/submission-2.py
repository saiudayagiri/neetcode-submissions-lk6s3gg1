class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                memo[(i,j)] = 1+dfs(i-1,j-1)
            else:
                memo[(i,j)] =max(dfs(i-1,j),dfs(i,j-1))
            return memo[(i,j)]
        return dfs(len(text1)-1,len(text2)-1)
        