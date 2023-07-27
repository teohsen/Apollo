from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low = 1
        high = sum(batteries)//n

        while low < high:
            target = high - (high - low)//2

            extra_power = sum(min(extra_power, target) for extra_power in batteries)
            if extra_power >= target * n:
                low = target
            else:
                high = target - 1

        return low

    def maxRunTimeAlt(self, n: int, batteries: List[int]) -> int:

        batteries.sort()

        extra = sum(batteries[:-n])  #[1,2,3]
        live = batteries[-n:]  # [4, 5]

        for i in range(n - 1):
            if extra // (i + 1) < live[i+1] - live[i]:
                return live[i] + extra // (i+1)

            extra -= (live[i+1] - live[i]) * (i+1)

        return live[-1] + extra //n
