class Solution:
    def maxDifference(self, s: str) -> int:
        freq=[0]*26
        for char in s:
            freq[ord(char)-ord("a")]+=1
        maxi=0
        mini=26
        for num in freq:
            if num%2:
                maxi=max(maxi,num)
            else:
                if num>0:
                    mini=min(mini,num)
        return maxi-mini
        