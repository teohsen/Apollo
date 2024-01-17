from typing import List
from collections import Counter, defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = Counter(arr).values()
        return len(arr) == len(set(arr))


    def uniqueOccurrences2(self, arr: List[int]) -> bool:
        x = defaultdict(int)
        for i in arr:
            x[i] += 1
        return len(x.values()) == len(set(x.values()))
