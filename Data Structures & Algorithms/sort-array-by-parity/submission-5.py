class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        for r in range(len(nums)):
            if nums[r]%2==0:
                nums[i],nums[r]=nums[r],nums[i]
                i+=1
        return nums

        