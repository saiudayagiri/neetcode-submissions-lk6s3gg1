class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not ("0"<=s[l]<="9" or "a"<=s[l]<="z" or "A"<=s[l]<="Z"):
                l+=1
            while l<r and not ("0"<=s[r]<="9" or "a"<=s[r]<="z"  or "A"<=s[r]<="Z"):
                r-=1 
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True               
        