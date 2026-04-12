class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(nums)-k+1):
            maxi=-11000
            for j in range(i,i+k):
                maxi=max(maxi,nums[j])
            res.append(maxi)
        return res

        