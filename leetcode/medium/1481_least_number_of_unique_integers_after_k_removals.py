from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        res = []

        for val, freq in Counter(arr).items():
            res.append(freq)

        res.sort()
        r = 0

        for i in res:
            k -= i
            if k >= 0:
                r += 1
            else:
                break

        return len(res) - r
