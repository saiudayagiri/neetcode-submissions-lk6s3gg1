class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        r = 0

        while r < len(flowerbed):
            # first position
            if r == 0 and flowerbed[r] == 0 and (r + 1 == len(flowerbed) or flowerbed[r + 1] == 0):
                res += 1
                r += 2

            # last position
            elif r == len(flowerbed) - 1 and flowerbed[r] == 0 and flowerbed[r - 1] == 0:
                res += 1
                r += 2

            # middle positions
            elif r > 0 and r < len(flowerbed) - 1 and flowerbed[r - 1] == flowerbed[r] == flowerbed[r + 1] == 0:
                res += 1
                r += 2

            else:
                r += 1

        return res >= n
