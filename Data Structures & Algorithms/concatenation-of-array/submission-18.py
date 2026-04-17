class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concatenatedResult = [0] * 2 * n
        for i in range(n):
            concatenatedResult[i] = nums[i]
            concatenatedResult[i + n] = nums[i]
        return concatenatedResult

        