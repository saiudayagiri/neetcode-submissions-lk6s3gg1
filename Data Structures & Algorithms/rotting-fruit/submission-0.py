class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        minutes = 0
        freshoranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    freshoranges+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        if freshoranges==0:
            return 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr,dc in directions:
                    nr = r+dr
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        freshoranges-=1
                        q.append((nr,nc))
            minutes+=1
        if freshoranges==0:
            return minutes-1
        return -1
                    
        