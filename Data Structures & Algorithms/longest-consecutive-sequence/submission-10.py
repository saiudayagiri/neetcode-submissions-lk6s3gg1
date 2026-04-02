class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in numsset:
                continue
            else:
                cnt = 0
                while num in numsset:
                    cnt += 1
                    num += 1
                longest = max(longest, cnt)
        return longest

        