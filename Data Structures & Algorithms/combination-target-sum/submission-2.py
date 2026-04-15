class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def bct(i,cursum,curarr):
            if cursum==target:
                res.append(curarr[:])
                return
            if i ==len(nums) or cursum>target:
                return
            curarr.append(nums[i])
            bct(i,cursum+nums[i],curarr)
            curarr.pop()
            bct(i+1,cursum,curarr)
            return
        bct(0,0,[])
        return res
        