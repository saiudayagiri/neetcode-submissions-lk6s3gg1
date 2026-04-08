class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        r = len(nums) - 1 
        j = 0
        while l <= r :
            if nums[l] == 0:
                nums[j], nums[l] = nums[l], nums[j]
                l+=1
                j+=1
            elif nums[l] == 2:
                nums[r], nums[l] = nums[l], nums[r]
                r-=1  
            else:
                l+=1
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        