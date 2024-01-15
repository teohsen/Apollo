from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        l_cache = {}
        w_cache = {}

        for w, l in matches:
            l_cache[l] = l_cache.get(l, 0) + 1
            w_cache[w] = w_cache.get(w, 0) + 1

        return [sorted(set(w_cache).difference(set(l_cache))), sorted([k for k, v in l_cache.items() if v == 1])]
