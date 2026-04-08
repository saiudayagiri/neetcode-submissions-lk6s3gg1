class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt=[0]*(max(arr) + 1)
        for num in arr:
            cnt[num]+=1
        for i in range(len(cnt)-1,0,-1):
            if i==cnt[i]:
                return i
        return -1

        