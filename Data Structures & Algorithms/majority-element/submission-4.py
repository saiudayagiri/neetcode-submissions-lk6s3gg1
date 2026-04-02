class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me=nums[0]
        cnt=0
        for num in nums:
            if num==me:
                cnt+=1
            else:
                cnt-=1
                if cnt<0:
                    cnt=1
                    me=num
        return me
        