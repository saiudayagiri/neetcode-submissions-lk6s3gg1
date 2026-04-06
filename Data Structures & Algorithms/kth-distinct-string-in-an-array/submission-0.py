class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm=defaultdict(int)
        for char in arr:
            hm[char]+=1
        for char in arr:
            if hm[char]==1:
                k-=1
                if k==0:
                    return char
        return ""
        