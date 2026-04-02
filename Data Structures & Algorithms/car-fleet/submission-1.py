class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        postime=[]
        for i in range(len(position)):
            postime.append((position[i],(target-position[i])/speed[i]))
        postime.sort(reverse=True)
        fleets=0
        prevtime=0
        for tup in postime:
            if tup[1]>prevtime:
                fleets+=1
                prevtime=tup[1]
        return fleets            
        

        