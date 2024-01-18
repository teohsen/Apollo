class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def helper(i):
            if cache.get(i):
                return cache.get(i)
            if i < 0:
                return 0
            if i == 0:
                return 1

            cache[i] = helper(i-1) + helper(i-2)

            return cache[i]

        return helper(n)


    def climbStairs2(self, n: int) -> int:

        cache = {
            1: 1,
            2: 2
        }

        def helper(i):
            if cache.get(i):
                return cache.get(i)

            cache[i] = helper(i-1) + helper(i-2)

            return cache[i]

        return helper(n)