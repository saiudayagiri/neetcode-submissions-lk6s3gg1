class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm={}
        for i,num in enumerate(nums1):
            hm[num]=i
        res=[-1]*len(nums1)
        stack=[]
        for num in nums2:
            while stack and num>stack[-1]:
                if stack[-1] in hm:
                    res[hm[stack[-1]]]=num
                stack.pop()
            stack.append(num)
        return res
        