class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        while numRows>1:
            currow=[1]*(len(res[-1])+1)
            prevrow=res[-1]
            for i in range(1,len(currow)-1):
                currow[i]=prevrow[i-1]+prevrow[i]
            res.append(currow)
            numRows-=1
        return res
        
        