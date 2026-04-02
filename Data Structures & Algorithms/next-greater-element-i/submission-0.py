class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        hm={}
        for i in range(len(nums1)):
            hm[nums1[i]]=i
        stack=[]
        for j in range(len(nums2)):
            while stack and nums2[j]>stack[-1]:
                res[hm[stack[-1]]]=nums2[j]
                stack.pop()
            if nums2[j] in hm:
                stack.append(nums2[j])
        return res


        