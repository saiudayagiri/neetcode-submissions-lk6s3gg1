class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        l = 0
        freq = {}
        res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            res = max(res, r - l + 1)

        return res
