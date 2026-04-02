class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def allpaths(i,j):
            if i==m-1 and j==n-1 :
                return 1
            if i>=m or j>=n:
                return 0
            return allpaths(i+1,j)+allpaths(i,j+1)
        return allpaths(0,0)            
        