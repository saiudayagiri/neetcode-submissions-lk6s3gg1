class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm={}
        for c in t:
            hm[c]=hm.get(c,0)+1
        required=len(hm)
        l=0
        hm2={}
        having=0
        res=s+s
        for r in range(len(s)):
            hm2[s[r]]=hm2.get(s[r],0)+1
            if s[r] in hm and hm2[s[r]]==hm[s[r]]:
                having+=1
            while having==required:
                if r-l+1<len(res):
                    res=s[l:r+1]
                if s[l] in hm and hm2[s[l]]==hm[s[l]]:
                    having-=1
                
                hm2[s[l]]-=1
                l+=1
        if res==s+s:
            return ""
        return res
                

        
        
        