class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_count = [0] * 26
        for char in s:
            chars_count[ord(char) - ord("a")] += 1
        for char in t:
            chars_count[ord(char) - ord("a")] -= 1
        for num in chars_count:
            if num != 0:
                return False
        return True

        