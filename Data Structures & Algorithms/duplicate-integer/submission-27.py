class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        numsset =set()
        for num in nums:
            if num in numsset:
                return True
            numsset.add(num)
    
        return False
        