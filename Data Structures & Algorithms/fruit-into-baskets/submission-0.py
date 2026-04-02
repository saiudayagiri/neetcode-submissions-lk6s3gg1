class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitset={}
        l=0
        res=0
        for r in range(len(fruits)):
            fruitset[fruits[r]]=fruitset.get(fruits[r],0)+1
            while len(fruitset)>2:
                fruitset[fruits[l]]-=1
                if fruitset[fruits[l]]==0:
                    del fruitset[fruits[l]]
                l+=1
            res=max(res,r-l+1)
        return res

        