class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0

        freq = {}
        l = 0
        count = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            if r - l + 1 > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            if r - l + 1 == k and len(freq) == k:
                count += 1

        return count
