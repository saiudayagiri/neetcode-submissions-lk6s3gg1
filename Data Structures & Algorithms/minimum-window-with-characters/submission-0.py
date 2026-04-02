class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_count = Counter(t)             # Map for t
        window_count = Counter()          # Map for common characters in s
        l = 0
        min_len = float('inf')
        res = ""

        for r in range(len(s)):
            if s[r] in t_count:            # Only care about common characters
                window_count[s[r]] += 1

            # Check if window satisfies t_count
            while all(window_count[c] >= t_count[c] for c in t_count):
                # Update result
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]
                
                if s[l] in window_count:
                    window_count[s[l]] -= 1
                l += 1

        return res
        