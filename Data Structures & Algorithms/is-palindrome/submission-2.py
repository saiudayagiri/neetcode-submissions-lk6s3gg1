class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            # Skip non-alphanumeric characters from the left side
            while l < r and not (ord('a') <= ord(s[l].lower()) <= ord('z') or ord('0') <= ord(s[l]) <= ord('9')):
                l += 1
            # Skip non-alphanumeric characters from the right side
            while r > l and not (ord('a') <= ord(s[r].lower()) <= ord('z') or ord('0') <= ord(s[r]) <= ord('9')):
                r -= 1
            # Compare characters (case insensitive)
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        