from typing import List
from functools import reduce
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = [1] * n


        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j] + 1)


        return max(res)

    def lengthOfLIS(self, nums: List[int]) -> int:
        def stage(l, q):
            print(l, q)
            i = bisect_left(l, q)

            print(i, l[:i])
            print(q, [q])
            print(i + 1, l[i + 1:])
            print(l[:i] + [q] + l[i + 1:])
            print("")
            return l[:i] + [q] + l[i + 1:]

        return len(reduce(lambda l, q: stage(l, q), nums, []))






