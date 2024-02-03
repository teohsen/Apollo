from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        Top down
        """
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            curr_max = 0
            res = 0
            for j in range(i, min(i+k, len(arr))):
                curr_max = max(curr_max, arr[j])
                win_size = j - i + 1
                res = max(res, dfs(j + 1) + curr_max * win_size)

            cache[i] = res
            return res

        return dfs(0)



    def maxSumAfterPartitioning2(self, arr: List[int], k: int) -> int:
        """
        Bottom Down
           pointers       j, i
        arr = [1, 2, 3, 4, 5, 6]
        """
        dp = [0] * k
        dp[0] = arr[0]

        for i in range(1, len(arr)):
            curr_max = 0
            max_at_i = 0
            for j in range(i,i-k,-1):
                if j < 0:
                    break

                curr_max = max(curr_max, arr[j])
                window_size = i - j + 1
                curr_sum = curr_max * window_size
                sub_sum = dp[(j - 1)%k] if j > 0 else dp[-1]
                max_at_i = max(max_at_i, curr_sum + sub_sum)

            dp[i % k] = max_at_i

        return dp[(len(arr)-1) % k]