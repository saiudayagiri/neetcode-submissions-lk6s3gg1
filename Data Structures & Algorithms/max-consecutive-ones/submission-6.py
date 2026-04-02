class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxcnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            maxcnt = max(maxcnt, cnt)
        return maxcnt
        