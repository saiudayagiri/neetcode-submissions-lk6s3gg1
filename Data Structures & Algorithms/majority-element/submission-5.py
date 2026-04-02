class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for num in nums:
            if count[num]>=n//2:
                return num
        