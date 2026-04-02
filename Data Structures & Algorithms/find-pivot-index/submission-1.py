class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot=sum(nums)
        cursum=0
        for r in range(len(nums)):
            if cursum==tot-cursum-nums[r]:
                return r
            cursum+=nums[r]
        return -1
        