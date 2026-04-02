class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row=[0]*len(picture)
        column=[0]*len(picture[0])
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j]=="B":
                    row[i]+=1
                    column[j]+=1
        res=0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j]=="B" and row[i]==1 and column[j]==1:
                    res+=1
        return res
                    

        