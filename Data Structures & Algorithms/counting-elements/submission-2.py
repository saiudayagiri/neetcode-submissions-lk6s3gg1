class Solution:
    def countElements(self, arr: List[int]) -> int:
        hm={}
        for num in arr:
            if num in hm:
                hm[num]+=1
            else:
                hm[num]=1
        cnt=0
        for num,cou in hm.items():
            if num+1 in hm:
                cnt+=hm[num]
        return cnt

        