class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if i!=j and nums[i]==nums[j]:
                    return True
        return False
   

        