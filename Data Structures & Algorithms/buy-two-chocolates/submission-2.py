class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mini1=float("inf")
        mini2=float("inf")
        for num in prices:
            if num<mini1:
                mini2=mini1
                mini1=num
            elif num<mini2:
                mini2=num
        if mini1+mini2>money:
            return money
        return money-mini1-mini2
        