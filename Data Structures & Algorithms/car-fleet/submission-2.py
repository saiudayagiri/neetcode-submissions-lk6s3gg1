class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posttime=sorted(zip(position,speed))
        fleets=0
        prevtime=0
        n=len(position)
        for i in range(n-1,-1,-1):
            if (target-posttime[i][0])/posttime[i][1] >prevtime:
                fleets+=1
                prevtime=(target-posttime[i][0])/posttime[i][1]
        return fleets        
            
        