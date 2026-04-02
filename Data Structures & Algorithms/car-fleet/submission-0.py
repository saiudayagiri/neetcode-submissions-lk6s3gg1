class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, [(target - p) / s for p, s in zip(position, speed)]), reverse=True)
        cnt = 0
        prev_t = 0  # Time of the last processed fleet
        
        for _, t in pair:  # We only care about time
            if t <= prev_t:  
                cnt += 1  # Merge with previous fleet
            else:
                prev_t = t  # This car becomes the new fleet leader
        
        return len(position) - cnt
        