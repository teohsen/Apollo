# Date : 05-05-2023
# Difficulty : Medium
# https://leetcode.com/problems/dota2-senate/

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                radiant.append(i)
            else:
                dire.append(i)

        senate_length = i + 1
        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()

            if d < r:
                dire.append(d + senate_length)
            else:
                radiant.append(r + senate_length)
        return "Radiant" if radiant else "Dire"