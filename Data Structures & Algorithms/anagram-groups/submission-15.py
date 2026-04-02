class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for char in string:
                arr[ord(char) - ord("a")] += 1
            res[tuple(arr)].append(string)
        return list(res.values())



        