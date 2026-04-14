class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        containerMap = {}
        for i,num in enumerate(nums):
            if target - num in containerMap:
                return [containerMap[target - num], i]
            containerMap[num] = i
                


        