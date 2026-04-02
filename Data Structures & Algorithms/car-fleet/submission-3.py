from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair position with time to reach target
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
        
        # sort by position (closer to target last)
        cars.sort(reverse=True)

        fleets = 0
        cur_time = 0  # last fleet's time

        for pos, time in cars:
            if time > cur_time:
                fleets += 1
                cur_time = time  # new fleet leader
            # else: merges with the current fleet

        return fleets
