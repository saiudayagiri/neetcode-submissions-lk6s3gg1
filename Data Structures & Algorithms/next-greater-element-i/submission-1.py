class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm={}
        for i in range(len(nums2)):
            ans=-1
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    ans=nums2[j]
                    break
            hm[nums2[i]]=ans
        res=[]
        for num in nums1:
            res.append(hm[num])
        return res
        