class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def func(i,path):
            if i==len(nums):
                res.append(path)
                return
            skip=func(i+1,path)
            include=func(i+1,path+[nums[i]])
        func(0,[])
        return res        
        