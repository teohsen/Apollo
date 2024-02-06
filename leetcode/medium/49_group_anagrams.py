from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]

        ord("a") = 97

        :param strs:
        :return:
        """
        cache = defaultdict(list)

        for word in strs:
            score = [0] * 26
            for c in word:
                score[ord(c) - 97] += 1

            cache[tuple(score)].append(word)


        return list(cache.values())


    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)

        for word in strs:
            cache["".join(sorted(word))].append(word)

        return list(cache.values())