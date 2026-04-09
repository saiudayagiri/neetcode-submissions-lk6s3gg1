class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m = r-(r-l)//2
            if m%2==0:
                m+=1
            if nums[m]!=nums[m-1]:
                r = m-1
            else:
                l=m + 1
        return nums[l]
        