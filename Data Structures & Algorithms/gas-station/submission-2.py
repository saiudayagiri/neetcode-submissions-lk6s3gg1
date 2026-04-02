class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        net = [gas[i] - cost[i] for i in range(n)]
        net = net + net  # duplicate to simulate circular path

        for start in range(n):
            fuel = 0
            completed = True
            for i in range(start, start + n):
                fuel += net[i]
                if fuel < 0:
                    completed = False
                    break
            if completed:
                return start
        return -1
        