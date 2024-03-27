from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # n = 3
        # trust = [[1, 3], [2, 3]]
        # trust = [[1,3],[2,3],[3,1]]
        #
        # trust = [[1,2],[2,3]]
        #
        # n = 1
        # trust = []

        cache = defaultdict(list)
        trust_any = defaultdict(list)

        for i in trust:
            cache[i[1]].append(i[0])
            trust_any[i[0]].append(i[1])

        result = []
        for k, v in cache.items():
            if len(v) == n-1 and k not in trust_any:
                result.append(k)

        return result[0] if len(result) == 1 else -1
