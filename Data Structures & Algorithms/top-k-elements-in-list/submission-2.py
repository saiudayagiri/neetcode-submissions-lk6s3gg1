class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        lst=[]
        for num,cnt in count.items():
            lst.append([cnt,num])
        lst=sorted(lst,reverse=True)
        result=[el[1] for el in lst[:k]]
        return result



        
        