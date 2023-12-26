class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        Top Down

        :param n:
        :param k:
        :param target:
        :return:
        """
        modu = 10**9 + 7
        cache = {}

        def rc(n , target):
            if n == 0:
                return 1 if target == 0 else 0
            if cache.get((n, target)) is not None:
                return cache.get((n, target))

            result = 0
            for val in range(1, k+1):
                result = (result + rc(n-1, target-val)) % modu


            cache[(n, target)] = result
            return result


        return rc(n, target)


    def numRollsToTarget2(self, n: int, k: int, target: int) -> int:
        """
        Bottom Up

        :param n:
        :param k:
        :param target:
        :return:
        """
        dp = [0] * (target + 1)  # dp[i] = num ways to roll i

        dp[0] = 1
        modu = 10**9 + 7

        for dice in range(n):
            next_dp = [0] * (target + 1)

            for val in range(1, k+1):
                for total_rolled in range(val, target+1):
                    next_dp[total_rolled] = (next_dp[total_rolled] + dp[total_rolled - val]) % modu


            dp = next_dp

        return dp[target]