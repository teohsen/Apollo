"""
https://leetcode.com/problems/reconstruct-itinerary/description/
"""
from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        cache = defaultdict(list)

        for src, dst in sorted(tickets):
            cache[src].append(dst)

        def dfs(loc):
            while cache[loc]:
                dfs(cache[loc].pop())
            result.append(loc)

        dfs("JFK")
        return result[::-1]

    def test(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        print(self.findItinerary(tickets))
