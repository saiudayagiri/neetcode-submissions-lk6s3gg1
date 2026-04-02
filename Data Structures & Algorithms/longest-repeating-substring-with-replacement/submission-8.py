class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr=[0]*26
        l=0
        res=0
        for r in range(len(s)):
            arr[ord(s[r])-ord("A")]+=1
            while max(arr)+k < r-l+1:
                arr[ord(s[l])-ord("A")]-=1
                l+=1
            res=max(res,r-l+1)
        return res
        