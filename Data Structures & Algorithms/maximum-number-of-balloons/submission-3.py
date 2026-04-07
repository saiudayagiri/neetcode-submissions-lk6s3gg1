class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp=defaultdict(int)
        for c in text:
            if c in "balon":
                mp[c]+=1
        
        mp["l"]=mp["l"]//2
        mp["o"]=mp["o"]//2
        return min(mp.values())
        
        