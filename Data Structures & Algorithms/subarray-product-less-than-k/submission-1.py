class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res=0
        cursum=1
        l=0
        for r in range(len(nums)):
            cursum*=nums[r]
            while l<=r and cursum>=k :
                cursum=cursum//nums[l]
                l+=1
            if cursum<k:
                res+=r-l+1
        return res
        