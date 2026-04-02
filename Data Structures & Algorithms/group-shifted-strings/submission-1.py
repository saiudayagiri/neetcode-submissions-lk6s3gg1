from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strings:
            key = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i-1])) % 26
                key.append(diff)
            groups[tuple(key)].append(s)

        return list(groups.values())
