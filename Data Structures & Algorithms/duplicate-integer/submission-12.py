class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numsset = set()
        for number in nums:
            if number in numsset:
                return True
            numsset.add(number)
        return False
        


    