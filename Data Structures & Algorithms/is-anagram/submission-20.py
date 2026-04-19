class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map_s = {}
        for char in s:
            char_map_s[char] = char_map_s.get(char, 0) + 1
        
        char_map_t = {}
        for char in t:
            char_map_t[char] = char_map_t.get(char, 0) + 1
        return char_map_s == char_map_t
        