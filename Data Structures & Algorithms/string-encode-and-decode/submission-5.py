class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res    

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            # find the delimiter #
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # s[i:j] gives the length
            res.append(s[j+1 : j+1+length])  # extract the word
            i = j + 1 + length  # move to next encoded word
        return res
