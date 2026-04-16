class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i, j):
            cnt=0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                cnt+=1
            return cnt
        
        res = 0
        for r in range(len(s)):
            # Odd length palindrome
            res+= expand(r, r)
            # Even length palindrome
            res+= expand(r, r+1)
            
            
        
        return res
        