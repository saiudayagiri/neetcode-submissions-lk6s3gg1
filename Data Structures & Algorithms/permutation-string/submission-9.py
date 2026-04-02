class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1=[0]*26
        arr2=[0]*26
        for ch in s1:
            arr1[ord(ch)-ord("a")]+=1
        l=0
        for r in range(len(s2)):
            arr2[ord(s2[r])-ord("a")]+=1
            if r-l+1>len(s1):
                arr2[ord(s2[l])-ord("a")]-=1
                l+=1
            if arr1==arr2:
                return True
        return False
        