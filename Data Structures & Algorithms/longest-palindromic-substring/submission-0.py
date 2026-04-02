class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        
        res = ""
        for r in range(len(s)):
            # Odd length palindrome
            temp1 = expand(r, r)
            # Even length palindrome
            temp2 = expand(r, r+1)
            
            # Update res if longer palindrome found
            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2
        
        return res
