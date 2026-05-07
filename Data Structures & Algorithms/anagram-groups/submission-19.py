class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_maps = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for char in string:
                arr[ord(char) - ord("a")] += 1
            anagram_maps[tuple(arr)].append(string)
        return list(anagram_maps.values())

        