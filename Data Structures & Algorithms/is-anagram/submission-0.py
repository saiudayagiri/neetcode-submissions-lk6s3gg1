class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*26
        for char in s:
            a[ord(char)-ord("a")]+=1
        for char in t:
            a[ord(char)-ord("a")]-=1
        for num in a:
            if num!=0:
                return False
        return True                

        