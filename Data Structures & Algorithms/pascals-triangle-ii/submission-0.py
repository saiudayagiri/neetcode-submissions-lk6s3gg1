class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev=[1]
        while rowIndex>0:
            cur=[1]*(len(prev)+1)
            for i in range(1,len(cur)-1):
                cur[i]=prev[i-1]+prev[i]
            prev=cur
            rowIndex-=1
        return prev
        