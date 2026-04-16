class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        def valid(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            for e in range(i+1,len(s)+1):
                if s[i:e] in words and valid(e):
                    memo[i]=True
                    return memo[i]
            memo[i]= False
            return memo[i]
        return valid(0)
        