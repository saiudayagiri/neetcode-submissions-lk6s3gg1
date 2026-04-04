class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt=0
        for i in range(len(flowerbed)):
            if i==0 and flowerbed[i]==0 and i+1<len(flowerbed) and flowerbed[i+1]==0:
                cnt+=1
                flowerbed[0]=1
            if i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                cnt+=1
                flowerbed[len(flowerbed)-1]=1
            if i+1 <len(flowerbed) and flowerbed[i]==flowerbed[i-1]==flowerbed[i+1]==0:
                cnt+=1
                flowerbed[i]=1
        return cnt>=n
        