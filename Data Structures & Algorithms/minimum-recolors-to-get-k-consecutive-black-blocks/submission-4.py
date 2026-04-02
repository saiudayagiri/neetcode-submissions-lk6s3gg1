class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        mini=float("inf")
        w=0
        for r in range(len(blocks)):
            if blocks[r]=="W":
                w+=1
            if r-l+1>k:
                if blocks[l]=="W":
                    w-=1
                l+=1

            if r-l+1==k:
                mini=min(mini,w)
        return mini
            

        