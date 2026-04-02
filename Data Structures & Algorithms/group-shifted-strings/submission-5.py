class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for string in strings:
            key=[]
            for i in range(1,len(string)):
                key.append((ord(string[i])-ord(string[i-1]))%26)
            res[tuple(key)].append(string)
        return list(res.values())
        