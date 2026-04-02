class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=0
        g.sort()
        s.sort()
        for num in s:
            if i<len(g) and num>=g[i]:
                i+=1
        return i

        