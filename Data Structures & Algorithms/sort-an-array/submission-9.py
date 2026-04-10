class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        count = [0] * 100001
        for num in nums:
            count[num + 50000] += 1
        j = 0
        for i, num in enumerate(count):
            while num > 0:
                res[j] = i - 50000
                num -= 1
                j += 1
        return res
