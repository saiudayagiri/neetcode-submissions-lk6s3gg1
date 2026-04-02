class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hm={}
        l=0
        res=0
        for r in range(len(s)):
            hm[s[r]]=hm.get(s[r],0)+1
            while len(hm)>2:
                hm[s[l]]-=1
                if hm[s[l]]==0:
                    del hm[s[l]]
                l+=1
            res=max(res,r-l+1)
        return res
                
        