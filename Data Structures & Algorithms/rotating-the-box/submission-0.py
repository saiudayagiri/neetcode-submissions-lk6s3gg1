class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS = len(boxGrid)
        COLS = len(boxGrid[0])
        
        # 1. Apply Gravity to each row
        for row in boxGrid:
            empty_pos = COLS - 1  # Start from the far right
            for i in range(COLS - 1, -1, -1):
                if row[i] == "#":
                    # Swap stone to the lowest available empty position
                    row[i], row[empty_pos] = row[empty_pos], row[i]
                    empty_pos -= 1
                elif row[i] == "*":
                    # Obstacle: the next stone must stay above (to the left of) it
                    empty_pos = i - 1
        
        # 2. Rotate the box 90 degrees clockwise
        # Original (ROWS x COLS) -> New (COLS x ROWS)
        res = [["." for _ in range(ROWS)] for _ in range(COLS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                # The row index becomes the column index (inverted)
                # The col index becomes the row index
                res[c][ROWS - 1 - r] = boxGrid[r][c]
                
        return res