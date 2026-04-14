class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxpos=0
        for i in range(len(nums)):
            if i>maxpos:
                return False
            maxpos=max(maxpos,i+nums[i])
        return True

        