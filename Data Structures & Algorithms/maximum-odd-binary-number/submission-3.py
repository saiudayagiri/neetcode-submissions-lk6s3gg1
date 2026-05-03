class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        for char in s:
            if char == "1":
                ones += 1
        start = "1" * (ones - 1) if ones - 1 > 0 else ""
        mid = "0" * (len(s) - ones)
        end = "1"
        return start + mid + end

        