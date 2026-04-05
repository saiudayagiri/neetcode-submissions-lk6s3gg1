class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxf=0
        l=0
        cursum=0
        for r in range(len(nums)):
            cursum+=nums[r]
            if cursum+k >= nums[r]*(r-l+1):
                maxf=max(maxf,r-l+1)
            else:
                cursum-=nums[l]
                l+=1
        return maxf



        