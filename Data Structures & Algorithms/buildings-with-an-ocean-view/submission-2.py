class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxsofar=0
        res=[]
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>maxsofar:
                res.append(i)
            maxsofar=max(maxsofar,heights[i])
        return res[::-1]
        