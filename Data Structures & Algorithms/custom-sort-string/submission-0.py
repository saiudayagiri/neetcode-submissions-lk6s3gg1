class Solution:
    def customSortString(self, order: str, s: str) -> str:
        arr=[0]*26
        for c in s:
            arr[ord(c)-ord("a")]+=1
        res=""
        for c in order:
            res+= c*arr[ord(c)-ord("a")]
            arr[ord(c)-ord("a")]=0
        for c in s:
            res+= c*arr[ord(c)-ord("a")]
            arr[ord(c)-ord("a")]=0
        return res
        
        