class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0] * n
        pos = 0
        neg = 1
        for x in nums:
            if x > 0:
                res[pos] = x
                pos += 2
            else:
                res[neg] = x
                neg += 2
        return res
