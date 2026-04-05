class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied=0
        maxsum=0
        cursum=0
        l=0
        for r in range(len(customers)):
            if r-l+1>minutes:
                if grumpy[l]:
                    cursum-=customers[l]
                l+=1

            if grumpy[r]==0:
                satisfied+=customers[r]
            else:
                cursum+=customers[r]
            maxsum=max(maxsum,cursum)
        return satisfied+maxsum


        