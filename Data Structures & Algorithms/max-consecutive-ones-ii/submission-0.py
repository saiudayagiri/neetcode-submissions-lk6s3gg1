class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones=0
        cntzeroes=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                cntzeroes+=1
            if cntzeroes>1:
                if nums[l]==0:
                    cntzeroes-=1
                l+=1
            maxones=max(maxones,r-l+1)
        return maxones
        