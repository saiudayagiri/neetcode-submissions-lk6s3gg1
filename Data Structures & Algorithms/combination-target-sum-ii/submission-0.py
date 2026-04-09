class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def bct(i,cursum,curarr):
            if cursum==target:
                res.append(curarr[:])
                return
            if cursum>target or i==len(candidates):
                return
            curarr.append(candidates[i])
            bct(i+1,cursum+candidates[i],curarr)
            curarr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            bct(i+1,cursum,curarr)
            return
        bct(0,0,[])
        return res
        