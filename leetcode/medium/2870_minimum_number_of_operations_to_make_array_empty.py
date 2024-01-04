from typing import List
from collections import Counter
from math import inf, ceil

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = {
            1: inf,
            2: 1,
            3: 1
        }
        nums = Counter(nums)
        for i in range(4, max(nums.values())+1):
            cache[i] = 1 + min(cache[i - 2], cache[i - 3])


        result = sum([cache[k] for k in nums.values()])
        return result if result < inf else -1

    def minOperations2(self, nums: List[int]) -> int:
        """
        """
        def actions(i):
            if i < 2:
                return inf

            d, r = i // 3, i % 3
            return d + (1 if r == 1 else r//2)

        result = 0
        for i in Counter(nums).values():
            result += actions(i)

        return result if not result == inf else -1

    def minOperations2(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=_AcO35R0fss&ab_channel=NeetCodeIO  #2
        :param nums:
        :return:
        """
        count = Counter(nums)
        res = 0
        for n, c in count.items():
            if c == 1:
                return -1

            res += ceil(c / 3)

        return res

    def minOperations3(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=_AcO35R0fss&ab_channel=NeetCodeIO  #1

        DP, Fibona, memo

        Time: O(N + X) , N is size of nums array, X is Memo
        Mem:
        :param nums:
        :return:
        """

        cache = {}
        def dfs(n):
            if n < 0 :
                return float("inf")
            if n in [2, 3]:
                return 1
            if n in cache:
                return cache[n]

            res = min(dfs(n-2),dfs(n-3))
            if res == -1:
                return -1
            cache[n] = 1 + res
            return res + 1

        count = Counter(nums)
        res = 0
        for n, c in count.items():
            op = dfs(c)
            if op == float("inf"):
                return -1
            res += op
        return res






