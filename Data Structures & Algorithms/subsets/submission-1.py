class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bct(i,cur):
            if i==len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            bct(i+1,cur)
            cur.pop()
            bct(i+1,cur)
            return 
        bct(0,[])
        return res
            
        