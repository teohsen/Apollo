# Date : 06-05-2023
# Difficulty : Medium
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

class Solution:

    vowels = frozenset("aeiou")

    def maxVowels(self, s: str, k: int) -> int:
        ans = cur = sum(s[i] in self.vowels for i in range(k))

        for idx in range(k, s.__len__()):
            cur += (s[idx] in self.vowels) - (s[idx - k] in self.vowels)
            ans = max(ans, cur)

        return ans
