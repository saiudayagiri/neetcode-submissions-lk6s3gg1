class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        freq = {}
        res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while len(freq) > 2:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            res = max(res, r - l + 1)

        return res
