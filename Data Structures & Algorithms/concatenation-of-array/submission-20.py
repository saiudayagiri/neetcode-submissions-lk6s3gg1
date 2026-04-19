class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concatenated_result = [0] * 2 * n
        for i in range(n):
            concatenated_result[i] = nums[i]
            concatenated_result[i + n] = nums[i]
        return concatenated_result

        