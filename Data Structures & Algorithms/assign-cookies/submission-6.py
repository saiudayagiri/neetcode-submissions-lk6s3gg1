class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=0
        g=sorted(g)
        s=sorted(s)
        for j in range(len(s)):
            if i<len(g) and  g[i]<=s[j]:
                i+=1
        return i

        