class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        res=0
        hm={}
        n=len(s)
        for r in range(n):
            hm[s[r]]=hm.get(s[r],0)+1
            while max(hm.values())+k<r-i+1:
                hm[s[i]]-=1
                i+=1
            res=max(res,r-i+1)
        return res        

        