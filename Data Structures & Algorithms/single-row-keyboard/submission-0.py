class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {ch: i for i, ch in enumerate(keyboard)}
        
        res = 0
        prev = keyboard[0]   # finger starts at index 0
        
        for c in word:
            res += abs(pos[c] - pos[prev])
            prev = c
        
        return res
