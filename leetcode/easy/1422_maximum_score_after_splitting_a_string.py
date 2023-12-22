class Solution:
    def maxScore(self, s: str) -> int:
        # s = "011101"
        # s = "1111"
        #s = "00111"
        max_score = 0

        for i in range(1, len(s)):
            max_score = max(s[:i].count("0") + s[i:].count("1"), max_score)

        return max_score


