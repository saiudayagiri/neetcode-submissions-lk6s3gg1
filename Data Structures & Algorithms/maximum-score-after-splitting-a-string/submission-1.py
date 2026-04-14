class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = 0
        ones = 0
        res = float("-inf")
        
        # Iterate only up to the second to last character
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeroes += 1
            else:
                ones += 1
            res = max(res, zeroes - ones)
        
        # Check the very last character only to update the total 'ones' count
        if s[-1] == "1":
            ones += 1
            
        return res + ones