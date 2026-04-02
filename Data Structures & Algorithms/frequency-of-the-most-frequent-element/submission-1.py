class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=0
        l=0
        cursum=0
        for r in range(len(nums)):
            cursum+=nums[r]
            while cursum+k < nums[r]*(r-l+1):
                cursum-=nums[l]
                l+=1
            res=max(res,r-l+1)
        return res

        