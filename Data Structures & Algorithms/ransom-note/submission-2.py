class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr=[0]*26
        for c in magazine:
            arr[ord(c)-ord("a")]+=1
        for c in ransomNote:
            arr[ord(c)-ord("a")]-=1
            if arr[ord(c)-ord("a")] <0:
                return False
        return True
        