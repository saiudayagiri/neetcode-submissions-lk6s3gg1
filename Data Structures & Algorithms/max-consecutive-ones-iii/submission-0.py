class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        cursum = 0

        for r in range(len(nums)):
            cursum += nums[r]

            if cursum + k < r - l + 1:
                cursum -= nums[l]
                l += 1

        return r - l + 1
