from math import inf
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        test = Counter(s)
        result = inf
        for i in [k for k, v in test.items() if v == 1]:
            result = min(result, s.index(i))

        return -1 if result == inf else result