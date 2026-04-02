class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False  # s1 can't be a permutation if it's longer than s2

        # Frequency arrays for s1 and s2
        s1_count = [0] * 26
        s2_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        
        # Initialize the first window
        for i in range(len(s1)):
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == s2_count:
            return True  # First window matches

        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            s2_count[ord(s2[i]) - ord('a')] += 1  # Add new char
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1  # Remove old char

            if s1_count == s2_count:
                return True

        return False
        