from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}  # (i, prev) -> []

        # nums = [1,2,5,15,45]
        def dfs(i, prev):
            if i == len(nums):
                return []
            if (i, prev) in cache:
                return cache[(i, prev)]

            res = dfs(i+1, prev) # skip nums[i]
            if nums[i] % prev == 0:
                tmp = [nums[i]] + dfs(i+1, nums[i]) # include num[i]
                res = tmp if len(tmp) > len(res) else res

            cache[(i, prev)] = res
            return res

        return dfs(0, 1)


    def largestDivisibleSubset2(self, nums: List[int]) -> List[int]:
        """
        TOP DOWN
        cache[i] = longest starting at i and including nums[i]

        :param nums:
        :return:
        """
        nums.sort()
        cache = {}

        def dfs(i):
            if i == len(nums):
                return []
            if i in cache:
                return cache[i]

            res = [nums[i]]
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dfs(j)
                    if len(tmp) > len(res):
                        res = tmp

            cache[i] = res
            return res

        res = []
        for i in range(len(nums)):
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp

        return res

    def largestDivisibleSubset3(self, nums: List[int]) -> List[int]:
        """
        Tabulation, btm-up

        :param nums:
        :return:
        """
        nums.sort()
        dp = [[n] for n in nums] # dp[i] = longest start at i
        res = []
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dp[j]
                    dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]

            res = dp[i] if len(dp[i]) > len(res) else res

        return res
