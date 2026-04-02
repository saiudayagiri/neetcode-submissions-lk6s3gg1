class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc=Counter(t)
        sc=Counter()
        l=0
        res=""
        minlent=float("inf")
        for r in range(len(s)):
            if s[r] in tc:
                sc[s[r]]+=1
            while all(sc[c]>=tc[c] for c in tc):
                if r-l+1<minlent:
                    minlent=r-l+1
                    res=s[l:r+1]
                if s[l] in sc:
                    sc[s[l]]-=1
                l+=1
        return res                

        