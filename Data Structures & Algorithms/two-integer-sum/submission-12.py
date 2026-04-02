class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexmap = {}
        for index,number in enumerate(nums):
            if target-number in indexmap:
                return [indexmap[target-number],index]
            indexmap[number]=index
        
        