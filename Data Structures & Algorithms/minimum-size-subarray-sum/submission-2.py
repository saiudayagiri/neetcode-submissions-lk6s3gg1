class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        res=float("inf")
        cursum=0
        for r in range(len(nums)):
            cursum+=nums[r]
            while cursum>=target:
                res=min(res,r-l+1)
                cursum-=nums[l]
                l+=1
        if res==float("inf"):
            return 0
        return res

        