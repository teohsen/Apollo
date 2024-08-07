from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]

        strs = ["tin", "ram", "zip", "cry", "pus", "jon", "zip", "pyx"]
        cache = defaultdict(list)
        for word in strs:
            r = [0] * 26
            for l in word:
                r[ord(l) - 97] += 1

            cache[tuple(r)].append(word)

        print(list(cache.values()))

        return list(cache.values())


    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        strs = ["tin", "ram", "zip", "cry", "pus", "jon", "zip", "pyx"]

        cache = defaultdict(list)
        for word in strs:
            cache["".join(sorted(word))].append(word)

        print(list(cache.values()))

        return list(cache.values())
