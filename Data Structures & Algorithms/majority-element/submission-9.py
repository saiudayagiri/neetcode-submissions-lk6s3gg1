class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        cur = None
        for num in nums:
            if num == cur:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    cnt = 1
                    cur = num
        return cur

        