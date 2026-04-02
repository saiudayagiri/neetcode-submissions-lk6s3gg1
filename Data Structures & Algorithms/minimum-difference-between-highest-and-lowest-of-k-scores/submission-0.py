class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mini=float("inf")
        l=0
        for r in range(len(nums)):
            if r-l+1>k:
                l+=1
            if r-l+1==k:
                mini=min(mini,nums[r]-nums[l])
        return mini

        