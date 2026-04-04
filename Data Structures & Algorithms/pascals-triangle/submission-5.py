class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
         
        while numRows-1 > 0:
            prev = res[-1]
            cur = [1]*(len(prev) + 1)
            for i in range(1,len(cur)-1):
                cur[i] = prev[i]+prev[i-1]
            res.append(cur)
            numRows-=1
        return res
        

        