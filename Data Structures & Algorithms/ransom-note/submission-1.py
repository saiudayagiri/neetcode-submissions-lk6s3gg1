class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm=[0]*26
        for c in magazine:
            hm[ord(c)-ord("a")]+=1
        for c in ransomNote:
            hm[ord(c)-ord("a")]-=1
            if hm[ord(c)-ord("a")]==-1:
                return False
        return True
        