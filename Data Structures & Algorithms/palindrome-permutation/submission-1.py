class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hm=[0]*26
        for c in s:
            hm[ord(c)-ord("a")]+=1
        cnt=0
        for num in hm:
            if num%2==1:
                cnt+=1
        return cnt<=1
        