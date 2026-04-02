class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm={}
        res=[]
        for i in range(len(nums1)):
            hm[nums2[i]]=i
        for num in nums1:
            res.append(hm[num])
        return res

        