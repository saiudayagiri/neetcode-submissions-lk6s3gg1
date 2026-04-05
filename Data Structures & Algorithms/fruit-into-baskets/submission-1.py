class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res=0
        l=0
        maps={}
        for r in range(len(fruits)):
            maps[fruits[r]]=maps.get(fruits[r],0)+1
            while len(maps)>2:
                maps[fruits[l]]-=1
                if maps[fruits[l]]==0:
                    del maps[fruits[l]]
                l+=1
            res=max(res,r-l+1)
        return res

        