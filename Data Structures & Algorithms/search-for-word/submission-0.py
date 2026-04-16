class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i,j,p):
            if p == len(word):
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[p]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            true = dfs(i+1,j,p+1) or dfs(i-1,j,p+1) or dfs(i,j+1,p+1) or dfs(i,j-1,p+1)
            board[i][j]=temp
            return true
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False


        