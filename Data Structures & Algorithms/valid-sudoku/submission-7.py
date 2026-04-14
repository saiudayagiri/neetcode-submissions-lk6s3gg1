class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if (i,"row",board[i][j]) in seen or (j,"col",board[i][j]) in seen or ((i//3,j//3),"box",board[i][j]) in seen:
                    return False
                seen.add((i,"row",board[i][j]))
                seen.add((j,"col",board[i][j]))
                seen.add(((i//3,j//3),"box",board[i][j]))
        return True
        