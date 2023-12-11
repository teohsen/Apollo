from typing import List
from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        #arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
        return Counter(arr).most_common(1)[0][0]

    def findSpecialInteger2(self, arr: List[int]) -> int:
        # arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
        threshold = len(arr)/4

        for i in set(arr):
            if arr.count(i) > threshold:
                return i
