class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot=sum(nums)
        cursum=0
        for i in range(len(nums)):
            if tot-cursum-nums[i]==cursum:
                return i
            cursum+=nums[i]
        return -1
        