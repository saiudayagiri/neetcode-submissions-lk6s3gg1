class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[i],nums[r]=nums[r],nums[i]
                i+=1
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        