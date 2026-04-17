class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            if i+1<len(s) and int(s[i:i+2])<=26:
                result=dfs(i+2) + dfs(i+1)
            else:
                result = dfs(i+1)
            memo[i] = result
            return memo[i]
        return dfs(0)
            
        