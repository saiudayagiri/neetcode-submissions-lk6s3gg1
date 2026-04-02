class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        cntT = {}
        for c in t:
            cntT[c] = cntT.get(c, 0) + 1

        cntS = {}
        have = 0
        required = len(cntT)

        res = ""
        resLen = float("inf")

        l = 0
        for r in range(len(s)):
            cntS[s[r]] = cntS.get(s[r], 0) + 1

            if s[r] in cntT and cntS[s[r]] == cntT[s[r]]:
                have += 1

            while have == required:
                # update result
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                # shrink window
                cntS[s[l]] -= 1
                if s[l] in cntT and cntS[s[l]] < cntT[s[l]]:
                    have -= 1

                l += 1

        return res
