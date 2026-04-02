class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        maxcnt=0
        for num in nums:
            if num==1:
                cnt+=1
                maxcnt=max(maxcnt,cnt)
            else:
                cnt=0
        return maxcnt
        