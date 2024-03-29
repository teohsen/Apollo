from typing import List
from bisect import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=JLoWc3v0SiE&ab_channel=NeetCodeIO
        :param startTime:
        :param endTime:
        :param profit:
        :return:
        """
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0

            if i in cache:
                return cache[i]

            # dont include at i
            res = dfs(i + 1)

            ##  include at i
            # Runtime exceed --> change to bisect
            # j = i +1
            # while j < len(intervals):
            #     if intervals[i][1] <= intervals[j][0]:
            #         break
            #     j += 1

            # intervals[i][1] to search from end time of current interval (i)
            # -1, -1
            j = bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)
