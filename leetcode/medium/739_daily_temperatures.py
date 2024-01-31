from collections import deque
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        deq = deque()

        for index, t in enumerate(temperatures):
            while deq and temperatures[deq[-1]] < t:
                i = deq.pop()
                result[i] = index - i
            deq.append(index)

        return result

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        # Bruteforce TLE
        n = len(temperatures)
        result = []

        for l in range(n):
            for r in range(l+1, n+1):
                if r == n:
                    result.append(0)
                    break

                if temperatures[r] >= temperatures[l]:
                    result.append(r-l)
                    break


        return result