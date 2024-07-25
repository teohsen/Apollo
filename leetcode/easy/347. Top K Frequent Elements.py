from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = Counter(nums)
        return [_[0] for _ in cache.most_common(k)]

