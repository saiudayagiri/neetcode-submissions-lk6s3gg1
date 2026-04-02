class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = [0] * len(nums)
        p = len(nums) - 1
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                res[p] = nums[l] ** 2
                l += 1
            else:
                res[p] = nums[r] ** 2
                r -= 1
            p -= 1
        return res


        