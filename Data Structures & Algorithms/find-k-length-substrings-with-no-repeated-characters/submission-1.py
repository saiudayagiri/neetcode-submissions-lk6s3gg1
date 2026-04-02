class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        charset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charset or r-l+1>k:
                if s[l] in charset:
                    charset.remove(s[l])
                l+=1
            charset.add(s[r])
            if r-l+1==k:
                res+=1
        return res
        