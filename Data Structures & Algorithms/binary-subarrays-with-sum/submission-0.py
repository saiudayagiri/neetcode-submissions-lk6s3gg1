class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt={0:1}
        cursum=0
        res=0
        for r in range(len(nums)):
            cursum+=nums[r]
            if cursum-goal in cnt:
                res+=cnt[cursum-goal]
            cnt[cursum]=cnt.get(cursum,0)+1
        return res
