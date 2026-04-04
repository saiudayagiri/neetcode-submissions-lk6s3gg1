class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_whites=k
        whites=0
        l=0
        for r in range(len(blocks)):
            if blocks[r]=="W":
                whites+=1
            if  r-l+1>k:
                if blocks[l]=="W":
                    whites-=1
                l+=1
            if r-l+1==k:
                min_whites=min(min_whites,whites)
        return min_whites
        