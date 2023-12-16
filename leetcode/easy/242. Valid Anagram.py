from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = Counter(s)
        t = Counter(t)

        return s == t

    def isAnagram2(self, s: str, t:str) -> bool:
        result = [0] * 26

        for i in s:
            result[ord(i) - 97] += 1

        for i in t:
            result[ord(i) - 97] -= 1

        return not any(result)