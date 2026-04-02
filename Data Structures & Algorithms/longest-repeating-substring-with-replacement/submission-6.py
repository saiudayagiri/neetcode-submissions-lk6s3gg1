class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        arr=[0]*26
        maxf=0
        for r in range(len(s)):
            arr[ord(s[r])-ord("A")]+=1
            maxf=max(maxf,arr[ord(s[r])-ord("A")])
            while r-l+1 >k+maxf:
                arr[ord(s[l])-ord("A")]-=1
                l+=1
            res=max(res,r-l+1)
        return res

        