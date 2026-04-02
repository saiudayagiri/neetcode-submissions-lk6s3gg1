class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_whites=float('inf')
        i=0
        white_count=0
        for r in range(len(blocks)):
            if blocks[r]=="W":
                white_count+=1
            if r-i+1 > k:
                if blocks[i]=="W":
                    white_count-=1
                i+=1
            if r-i+1 == k:
                min_whites=min(min_whites,white_count)
        return min_whites