class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        for word in strs:
            arr=[0]*26
            for c in word:
                arr[ord(c)-ord("a")]+=1
            hm[tuple(arr)].append(word)
        
        return list(hm.values())        
        