class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        n = len(nums)
        for i in range(n):
            target_num = target - nums[i]
            if target_num in nums_map:
                return [nums_map[target_num], i]
            nums_map[nums[i]] = i
        