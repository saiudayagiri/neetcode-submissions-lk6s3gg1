class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)  # Dictionary to store grouped anagrams
        
        for word in strs:
            a = [0] * 26  # Frequency array for letters a-z
            for char in word:
                a[ord(char) - ord("a")] += 1  # Count character occurrences
            
            hm[tuple(a)].append(word)  # Convert list to tuple for hashing
        
        return list(hm.values()) 
        