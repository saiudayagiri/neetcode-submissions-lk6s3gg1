class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm=[0]*501
        for num in arr:
            hm[num]+=1
        for i in range(500,0,-1):
            if i==hm[i]:
                return i
        return -1

        