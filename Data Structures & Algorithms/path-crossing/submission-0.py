class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # 1. Use a tuple for the origin and a set to store visited coordinates
        x, y = 0, 0
        visited = {(0, 0)}
        
        for move in path:
            # 2. Update coordinates based on direction
            if move == "N":
                y += 1
            elif move == "S":
                y -= 1
            elif move == "E":
                x += 1
            else: # move == "W"
                x -= 1
            
            # 3. Create a tuple of current position to check/add to set
            current_pos = (x, y)
            
            if current_pos in visited:
                return True
            
            visited.add(current_pos)
            
        return False