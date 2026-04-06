class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res=0
        l=0
        if len(nums)==1:
            return 1
        for r in range(1,len(nums)):
            if nums[r]<=nums[r-1]:
                l=r
            res=max(res,r-l+1)
        l=0
        for r in range(1,len(nums)):
            if nums[r]>=nums[r-1]:
                l=r
            res=max(res,r-l+1)
        return res
        
        