class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        numsset=set()
        for i in range(n):
            if nums[i] in numsset:
                return True
            numsset.add(nums[i])
        return False
   

        