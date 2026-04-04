class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        mini = nums[-1]-nums[0]
        for r in range(len(nums)):
            if r-l+1>k:
                l+=1
            if r-l+1==k:
                mini=min(mini,nums[r]-nums[l])
        return mini

        