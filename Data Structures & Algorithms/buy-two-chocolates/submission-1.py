class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mini1=float("inf")
        mini2=float("inf")
        for price in prices:
            if price <mini1:
                mini2=mini1
                mini1=price
            elif price<mini2:
                mini2=price
        if mini1==float("inf") or mini2==float("inf") or mini1+mini2>money:
            return money
        return money-mini1-mini2
        