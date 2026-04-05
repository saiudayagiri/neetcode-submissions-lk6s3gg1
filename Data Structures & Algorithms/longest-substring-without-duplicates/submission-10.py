class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        l=0
        maxlent=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            maxlent=max(maxlent,r-l+1)
            charset.add(s[r])
        return maxlent
        