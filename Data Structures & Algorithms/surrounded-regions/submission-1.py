class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != 'O':
                return
            board[r][c] = 'T'  # Temporarily mark as safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        rows, cols = len(board), len(board[0])
        
        # Start DFS from border 'O's
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # Flip all remaining 'O' to 'X', and revert 'T' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        