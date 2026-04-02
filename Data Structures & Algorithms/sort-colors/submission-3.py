class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        r=len(nums)-1
        j=0
        while j<=r:
            if nums[j]==0:
                nums[j],nums[l]=nums[l],nums[j]
                l+=1
                j+=1
            elif nums[j]==2:
                nums[j],nums[r]=nums[r],nums[j]
                r-=1
            else:
                j+=1
        return nums


        """
        Do not return anything, modify nums in-place instead.
        """
        