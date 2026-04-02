class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        arr=[0]*26
        for i in range(len(s)):
            arr[ord(s[i])-ord("a")]+=1
            arr[ord(t[i])-ord("a")]-=1
        return max(arr)==0 and min(arr)==0        

        