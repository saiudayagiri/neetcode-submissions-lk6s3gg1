class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        seen=set()
        res=0
        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[i])
                    i+=1
            seen.add(s[r])        
            res=max(res,r-i+1)
        return res            
        