from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = collections.Counter(nums)

        return [x[0] for x in sol.most_common(k)]

