class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n * 2
        for i in range(n):
            res[i] = nums[i]
            res[n + i] = nums[i]
        return res
        