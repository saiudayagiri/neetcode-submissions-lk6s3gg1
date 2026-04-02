class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                left = (i == 0 or flowerbed[i - 1] == 0)
                right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if left and right:
                    count += 1
                    i += 2
                    continue

            i += 1

        return count >= n
