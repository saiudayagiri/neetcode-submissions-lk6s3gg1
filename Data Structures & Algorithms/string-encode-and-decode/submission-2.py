class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the separator to extract the length
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1  # move past '#'
            res.append(s[j:j + length])
            i = j + length  # move to the next encoded string
        return res
