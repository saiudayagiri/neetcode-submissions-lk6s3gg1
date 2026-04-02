class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueset=set()
        for num in nums:
            if num in uniqueset:
                return True
            else:
                uniqueset.add(num)
        return False        
         